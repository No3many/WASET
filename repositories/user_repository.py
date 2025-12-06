from core.db_singleton import DatabaseConnection
from models.user import User

class UserRepository:
    def __init__(self):
        # بنستلم خط الاتصال من الـ Singleton
        self.connection = DatabaseConnection().get_connection()

    def add_user(self, username, email, password_hash, role):
        cursor = self.connection.cursor()
        query = "INSERT INTO users (username, email, password_hash, role) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (username, email, password_hash, role))
        self.connection.commit()
        cursor.close()
        print(f"User {username} added successfully!")

    def get_user_by_email(self, email):
        cursor = self.connection.cursor(dictionary=True) # dictionary=True عشان النتيجة ترجع كـ dict
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return User(row['id'], row['username'], row['email'], row['password_hash'], row['role'])
        return None