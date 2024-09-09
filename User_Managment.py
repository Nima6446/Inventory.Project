import bcrypt
import sqlite3


class User_Manager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def authenticate_user(self, username, password):
        try:
            self.db_manager.cursor.execute('SELECT role, password FROM users WHERE username = ?', (username,))
            user = self.db_manager.cursor.fetchone()
            if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
                return user[0]
            return None
        except sqlite3.Error as error:
            print(f"خطا در تایید کاربر: {error}")
            return None

    def add_user(self, username, password, role):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            self.db_manager.cursor.execute('''
            INSERT INTO Users (username, password, role) 
            VALUES (?, ?, ?)
            ''', (username, hashed_password.decode('utf-8'), role))
            self.db_manager.commit()
            print("کاربر با موفقیت اضافه شد.")
        except sqlite3.Error as error:
            print(f"خطا در اضافه کردن کاربر: {error}")

    def delete_user(self, User_ID):
        try:
            self.db_manager.cursor.execute('''
            DELETE FROM Users WHERE ID = ?
            ''', (User_ID,))
            self.db_manager.commit()
            print("کاربر با موفقیت حذف شد.")
        except sqlite3.Error as error:
            print(f"خطا در حذف کاربر: {error}")

    def show_all_users(self):
        try:
            self.db_manager.cursor.execute('''
            SELECT id, username, role FROM Users
            ''')
            users = self.db_manager.cursor.fetchall()
            if users:
                print("لیست کاربران:")
                for User in users:
                    print(f'User ID: {User[0]}, Username: {User[1]}, Role: {User[2]}')
            else:
                print("هیچ کاربری در سیستم وجود ندارد.")
        except sqlite3.Error as error:
            print(f"خطا در نمایش کاربران: {error}")
