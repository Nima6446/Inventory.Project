import sqlite3


class Category_Manager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_category(self, name):
        self.db_manager.cursor.execute('''INSERT INTO Categories (name) VALUES (?)''', (name,))
        self.db_manager.commit()
        print("دسته‌بندی با موفقیت اضافه شد.")
        print("//////////////////////////////////")

    def show_all_categories(self):
        try:
            self.db_manager.cursor.execute('''SELECT id , name FROM categories''')
            Categories = self.db_manager.cursor.fetchall()
            if Categories:
                for Category in Categories:
                    print(f"Category ID : {Category[0]} , name : {Category[1]}")
            else:
                print("هیچ دسته‌بندی‌ای وجود ندارد.")
                print("//////////////////////////////////")
        except sqlite3.Error as error:
            print("خطا در نمایش دسته‌بندی‌ها: {error}")
            print("//////////////////////////////////")

    def delete_category(self, Category_ID):
        try:
            self.db_manager.cursor.execute('''
                   DELETE FROM Categories WHERE id = ?
               ''', (Category_ID,))
            self.db_manager.commit()
            print("دسته‌بندی با موفقیت حذف شد.")
            print("//////////////////////////////////")
        except sqlite3.Error as error:
            print(f"خطا در حذف دسته‌بندی: {error}")
            print("//////////////////////////////////")
