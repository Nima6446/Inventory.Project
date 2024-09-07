import sqlite3
from datetime import datetime


class Order_Manager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def delete_order(self, Order_ID):
        try:
            self.db_manager.cursor.execute('''
                  DELETE FROM orders WHERE id = ?
              ''', (Order_ID,))
            self.db_manager.commit()
            print("سفارش با موفقیت حذف شد.")
            print("//////////////////////////////////")
        except sqlite3.Error as error:
            print(f"خطا در حذف سفارش: {error}")
            print("//////////////////////////////////")

    def add_order(self, person, Product_ID, quantity, price, order_type):
        date = datetime.now().strftime("%Y-%m-%d")

        try:
            # اضافه کردن سفارش به جدول Orders
            self.db_manager.cursor.execute('''
            INSERT INTO Orders (person, Product_ID, quantity, price, order_type, date)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (person, Product_ID, quantity, price, order_type, date))

            # به‌روزرسانی موجودی محصول
            if order_type == "in":
                self.db_manager.cursor.execute('''
                UPDATE Products SET quantity = quantity + ? WHERE ID = ?
                ''', (quantity, Product_ID))

            elif order_type == "out":
                self.db_manager.cursor.execute('''
                UPDATE Products SET quantity = quantity - ? WHERE ID = ?
                ''', (quantity, Product_ID))

            self.db_manager.commit()
            print("سفارش شما با موفقیت ثبت شد.")

        except sqlite3.Error as error:
            print(f"خطا در ثبت سفارش: {error}")

    def show_orders_history(self):
        try:
            self.db_manager.cursor.execute('''
               SELECT Orders.ID, Orders.person, Products.name, Orders.quantity, Orders.price, Orders.order_type, Orders.date
               FROM Orders
               JOIN Products ON Orders.Product_ID = Products.ID
               ''')
            orders = self.db_manager.cursor.fetchall()

            if orders:
                print("تاریخچه سفارش‌ها:")
                for order in orders:
                    print(f'Order ID: {order[0]}, Person: {order[1]}, Product: {order[2]}, Quantity: {order[3]}, '
                          f'Price: {order[4]}, Type: {order[5]}, Date: {order[6]}')
            else:
                print("هیچ سفارشی ثبت نشده است.")

        except sqlite3.Error as error:
            print(f"خطا در نمایش تاریخچه سفارش‌ها: {error}")
