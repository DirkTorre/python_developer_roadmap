import sqlite3

class DataBase:
    def __init__(self):
        self.data = {}
    
    def add_user(self, user_id, name):
        if user_id in self.data:
            raise ValueError("User already exists")
        self.data[user_id] = name
    
    def get_user(self, user_id):
        return self.data.get(user_id, None)

    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]


def save_user(name, age):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name,age) VALUES (?,?)", (name, age))
    conn.commit()
    conn.close()