


import sqlite3

class UniversityDB:
    def __init__(self, db_name="university.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def execute(self, query, params=None):
        if params:
            self.cur.execute(query, params)
        else:
            self.cur.execute(query)
        self.conn.commit()

    def fetchall(self, query, params=None):
        self.execute(query, params)
        return self.cur.fetchall()

    def close(self):
        self.conn.close()

    def setup(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
            );
        """)
        self.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(id)
            );
        """)
        self.execute("""
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
            );
        """)
        self.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
            );
        """)
        self.execute("""
        CREATE TABLE IF NOT EXISTS enrollments(
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
            );
        """)

    def add_department(self, name):
        self.execute("INSERT INTO departments (name) VALUES (?)", (name,))

    def add_teacher(self, name, department_id):
        self.execute("INSERT INTO teachers (name, department_id) VALUES (?, ?)", (name, department_id))

    def add_course(self, title, teacher_id):
        self.execute("INSERT INTO courses (title, teacher_id) VALUES (?, ?)", (title, teacher_id))

    def add_student(self, name):
        self.execute("INSERT INTO students (name) VALUES (?)", (name, ))

    def enrool_student(self, student_id, course_id):
        self.execute("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

    def course_student_stats(self):
        return self.fetchall("""
            SELECT c.title, COUNT(e.student_id) as student_count
            FROM courses c 
            LEFT JOIN enrollments e ON c.id = e.course_id
            GROUP BY c.id
        """)

    def active_students(self):
        return self.fetchall("""
            SELECT name FROM students
            WHERE id IN (
                SELECT student_id
                FROM enrollments
                GROUP BY student_id
                HAVING COUNT(course_id) >= 2
            )
        """)

    def create_student_course_view(self):
        self.execute("""
            CREATE VIEW IF NOT EXISTS student_course_view AS
            SELECT s.name AS student_name, c.title AS course_title
            FROM students s
            JOIN enrollments e ON s.id = e.student_id
            JOIN courses c ON e.course_id = c.id
        """)

    def get_student_course_view(self):
        return self.fetchall("SELECT * FROM student_course_view")


db = UniversityDB()
db.setup()

db.add_department("Compiuter Scince")
db.add_teacher("Dr. Smith", 1)
db.add_teacher("Dr. Bob", 1)

db.add_course("Python Back-End", 1)
db.add_course("Algorithms", 2)

db.add_student("Ali")
db.add_student("Bob")

db.enrool_student(1, 1)
db.enrool_student(1, 2)
db.enrool_student(2, 1)

print("Кол-ВО студентов на каждом курсе")
for title , count in db.course_student_stats():
    print(f"Курс : {title}, студентов {count}")

print("Студенты записанные на 2+ курса")
for (name, ) in db.active_students():
    print(f"{name}")

db.create_student_course_view()
print("Представление студент-курс")
for student_name, course_title in db.get_student_course_view():
    print(f"{student_name} -> {course_title}")

db.close()