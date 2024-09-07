import sqlite3


class Product_Manager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def delete_product(self, Product_ID):
        try:
            self.db_manager.cursor.execute('''
                DELETE FROM products WHERE id = ?
            ''', (Product_ID,))
            self.db_manager.commit()
            print("محصول با موفقیت حذف شد.")
            print("//////////////////////////////////")
        except sqlite3.Error as error:
            print(f"خطا در حذف محصول: {error}")
            print("//////////////////////////////////")

    def add_product(self, name, color, storage, RAM, region, quantity, Brand_ID):
        (self.db_manager.cursor.execute('''
        INSERT INTO Products (name,color,storage,RAM,region,quantity,Brand_ID)
        VALUES (?,?,?,?,?,?,?)''',(name, color, storage, RAM, region, quantity, Brand_ID)))
        self.db_manager.commit()
        print("محصول با موفقیت اضافه شد.")
        print("//////////////////////////////////")


    def show_products(self):
        try:
            self.db_manager.cursor.execute('''
            SELECT Products.ID, Products.name, Products.color, Products.storage, Products.RAM, Products.region, Products.quantity,
            Brands.name AS brand_name, Categories.name AS category_name
            FROM Products
            JOIN Brands ON Products.Brand_ID = Brands.ID
            JOIN Categories ON Brands.Category_ID = Categories.ID
            ''')
            products = self.db_manager.cursor.fetchall()

            if products:
                for product in products:
                    print(
                        f'Product ID: {product[0]}, Name: {product[1]}, Color: {product[2]}, Storage: {product[3]}GB, '
                        f'RAM: {product[4]}, Region: {product[5]}, Quantity: {product[6]}, Brand: {product[7]}, Category: {product[8]}')
            else:
                print("هیچ محصولی وجود ندارد.")

        except sqlite3.Error as error:
            print(f"خطا در نمایش محصولات: {error}")

    def get_low_stock_products(self, threshold):
        try:
            self.db_manager.cursor.execute('SELECT name, quantity FROM products WHERE quantity < ?', (threshold,))
            products = self.db_manager.cursor.fetchall()
            if products:
                print("محصولات با موجودی کم:")
                for product in products:
                    print(f'Product: {product[0]}, Quantity: {product[1]}')
                    print("//////////////////////////////////")
            else:
                print("محصولی با موجودی کم وجود ندارد.")
                print("//////////////////////////////////")
        except sqlite3.Error as error:
            print(f"خطا در نمایش محصولات با موجودی کم: {error}")
            print("//////////////////////////////////")

    def search_product(self, product_name):
        try:
            self.db_manager.cursor.execute("SELECT * FROM Products WHERE name LIKE ?", ('%' + product_name + '%',))
            Products = self.db_manager.cursor.fetchall()
            if Products:
                for product in Products:
                    print(f"ID: {product[0]}")
                    print(f"Name: {product[1]}")
                    print(f"Price: {product[2]}")
                    print(f"Quantity: {product[3]}")
                    print(f"Description: {product[4]}")
                    print(f"Brand: {product[5]}")
                    print("-----------------------------")
            else:
                print("هیچ محصولی با این نام یافت نشد.")

        except sqlite3.Error as error:
            print(f"خطا در جستجوی محصول: {error}")
