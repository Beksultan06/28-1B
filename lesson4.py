


import sqlite3


class UserDatabase:
    def __init__(self, db_name='users.db'):
        self.connection = sqlite3.connect(db_name)
        self.curcor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.curcor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    def add_user(self, name: str, age: int):
        self.curcor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        self.connection.commit()

    def get_all(self):
        self.curcor.execute('SELECT * FROM users')
        return self.curcor.fetchall()

    def user_by_name(self, name: str):
        self.curcor.execute('SELECT * FROM users WHERE name = ?', (name,))
        return self.curcor.fetchall()

    def close(self):
        self.connection.close()

db = UserDatabase()

db.add_user("Bob", 45)
db.add_user("ALihan", 13)

for user in db.get_all():
    print(user)

for user in db.user_by_name("Bob"):
    print(user)

db.close()