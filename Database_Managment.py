import sqlite3
from datetime import datetime


#مدیریت دیتا بیس
class Database_Manager:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as error:
            print()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            name TEXT NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Brands(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            Category_ID INTEGER NOT NULL,
            FOREIGN KEY (Category_ID) REFERENCES Categories(ID)
            )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            storage INTEGER NOT NULL,
            RAM INTEGER NOT NULL,   
            region TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            Brand_ID INTEGER NOT NULL,
            FOREIGN KEY (Brand_ID) REFERENCES Brands(ID)
            )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password  NOT NULL,
            role TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            person TEXT NOT NULL,
            Product_ID INTEGER NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            order_type TEXT NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (Product_ID) REFERENCES Products(ID)
             )
        ''')

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
