import sqlite3


class Brand_Manager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def delete_brand(self, Brand_ID):
        try:
            self.db_manager.cursor.execute('''
                  DELETE FROM brands WHERE id = ?
              ''', (Brand_ID,))
            self.db_manager.commit()
            print("برند با موفقیت حذف شد.")
            print("//////////////////////////////////")
        except sqlite3.Error as error:
            print(f"خطا در حذف برند: {error}")
            print("//////////////////////////////////")

    def add_brand(self, name, Category_ID):
        self.db_manager.cursor.execute('''
        INSERT INTO brands (name, Category_ID) VALUES (?, ?)''', (name, Category_ID))
        self.db_manager.commit()
        print("برند با موفقیت اضافه شد.")
        print("//////////////////////////////////")

    def show_brands(self):
        try:
            self.db_manager.cursor.execute('''
                SELECT Brands.ID, Brands.Name, Categories.Name AS Category_Name
                FROM Brands
                JOIN Categories ON Brands.Category_ID = Categories.ID
            ''')
            brands = self.db_manager.cursor.fetchall()

            if not brands:
                print("هیچ برندی موجود نیست.")
            else:
                for brand in brands:
                    print(f"Brand ID: {brand[0]}, Name: {brand[1]}, Category: {brand[2]}")
        except Exception as error:
            print(f"خطا در دریافت برندها: {error}")



