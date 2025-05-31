import sqlite3 


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT,
            phone TEXT,
            city TEXT 
        )
        """)
        self.connection.commit()

    def add_user(self, name, age, email, phone, city):
        self.cursor.execute("""
        INSERT INTO users(name, age, email, phone, city)
        VALUES (?, ?, ?, ?, ?)""", (name, age, email, phone, city))
        self.connection.commit()

    def get_users(self):
        self.cursor.execute("select * from users")
        return self.cursor.fetchall()

    def find_by_user(self, name):
        self.cursor.execute("SELECT * FROM users WHERE name LIKE ?", (f"%{name}%",))
        return self.cursor.fetchall()

    def updateuser_age(self, user_id, new_age):
        self.cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()


def print_user(user):
    print(f"""
    ID: {user[0]}
    NAME: {user[1]}
    AGE: {user[2]}
    EMAIL: {user[3]}
    PHONE: {user[4]}
    CITY: {user[5]} 
""")

if __name__ == "__main__":
    db = Database("users.db")

    while True:
        print("""
        Menu
        1. Added users
        2. GET ALL users
        3. UPDATE users
        4. DELETE users
        5. GET users name
        0. Exit
    """)
        choices = input("Выберите действия: ")

        if choices == "1":
            name = input("Name: ")
            age = input("age: ")
            email = input("email: ")
            phone = input("phone: ")
            city = input("city: ")
            db.add_user(name, age, email, phone, city)
            print("OK")
        
        elif choices == "2":
            users = db.get_users()
            if not users:
                print("Not user")
            for user in users:
                print_user(user)

        elif choices == '3':
            user = int(input("Enter user id: "))
            new_age = int(input("New AGE: "))
            db.updateuser_age(user, new_age)
            print("UPDATE user age")

        elif choices == "4":
            user_id = int(input("Enter users id: "))
            db.delete_user(user_id)
            print("DELETE user")

        elif choices == "5":
            name = input("Enter name user: ")
            results = db.find_by_user(name)
            if results:
                for user in results:
                    print_user(user)
            else:
                print("Not user")

        elif choices == "0":
            db.close()
            print("EXIT")
            break

        else:
            print("Неверный выбор Попробуй снова")