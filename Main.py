from Database_Managment import Database_Manager
from Category_Managment import Category_Manager
from Brand_Managment import Brand_Manager
from Product_Managment import Product_Manager
from Order_Managment import Order_Manager
from User_Managment import User_Manager

db = Database_Manager(r'E:\Terminal\Inventory_Managment\inventory.db')

category_manager = Category_Manager(db)
brand_manager = Brand_Manager(db)
product_manager = Product_Manager(db)
order_manager = Order_Manager(db)
user_manager = User_Manager(db)


def return_to_menu():
    input("\nجهت برگشت به منوی اصلی Enter را فشار دهید...")


# Security
authenticated = False
while not authenticated:
    username = input("نام کاربری خود را وارد کنید: ")
    password = input("رمز عبور خود را وارد کنید: ")
    role = user_manager.authenticate_user(username, password)
    if role:
        print(f"ورود با موفقیت. خوش آمدید {username}.")
        authenticated = True
    else:
        print("نام کاربری یا رمز عبور اشتباه است. لطفاً دوباره تلاش کنید.")

input("جهت وارد شدن به منوی اصلی Enter را فشار دهید")
while True:
    print("\033[30;43m دسته بندی \033[0m")
    print("1. اضافه کردن دسته‌بندی")
    print("2. نمایش دسته‌بندی‌ها")
    print("3. حذف دسته‌بندی")
    print("//////////////////////////////////")
    print("\033[30;43m برند \033[0m")
    print("4. اضافه کردن برند")
    print("5. نمایش برندها")
    print("6. حذف برند")
    print("//////////////////////////////////")
    print("\033[30;43m کالا \033[0m")
    print("7. اضافه کردن کالا")
    print("8. نمایش کالاها")
    print("9. حذف کالا")
    print("10. جست و جوی کالا")
    print("11. نمایش کالا با موجودی کم")
    print("//////////////////////////////////")
    print("\033[30;43m سفارش \033[0m")
    print("12. ثبت سفارش")
    print("13. نمایش تاریخچه سفارش‌ها")
    print("14. حذف سفارش")
    print("//////////////////////////////////")
    print("\033[30;43m کاربر \033[0m")
    print("15. اضافه کردن کاربر")
    print("16. حذف کاربر")
    print("17. نمایش کاربر ها")
    print("//////////////////////////////////")
    print("\033[41m خروج \033[0m")
    print("18. خروج")

    choice = input("گزینه خود را وارد کنید: ")

    if choice == '1':  # اضافه کردن دسته‌بندی
        name = input("نام دسته‌بندی را وارد کنید: ")
        category_manager.add_category(name)
        return_to_menu()
    elif choice == '2':  # نمایش همه دسته‌بندی‌ها
        category_manager.show_all_categories()
        return_to_menu()
    elif choice == '3':  # حذف دسته‌بندی
        Category_ID = int(input("آی‌دی دسته‌بندی را وارد کنید: "))
        category_manager.delete_category(Category_ID)
        return_to_menu()
    elif choice == '4':  # اضافه کردن برند
        name = input("نام برند را وارد کنید: ")
        Category_ID = int(input("آی‌دی دسته‌بندی مربوط به این برند را وارد کنید: "))
        brand_manager.add_brand(name, Category_ID)
        return_to_menu()
    elif choice == '5':  # نمایش برندها
        brand_manager.show_brands()
        return_to_menu()
    elif choice == '6':  # حذف برند
        Brand_ID = int(input("آی‌دی برند را وارد کنید: "))
        brand_manager.delete_brand(Brand_ID)
        return_to_menu()
    elif choice == '7':  # اضافه کردن محصول
        name = input("نام محصول را وارد کنید: ")
        color = input("رنگ محصول را وارد کنید: ")
        storage = int(input("حجم ذخیره‌سازی محصول (در گیگابایت) را وارد کنید: "))
        RAM = int(input("رم را وارد کنید"))
        region = input("ریحن را وارد کنید")
        quantity = int(input("تعداد محصول را وارد کنید: "))
        Brand_ID = int(input("آی‌دی برند مربوط به این محصول را وارد کنید: "))
        product_manager.add_product(name, color, storage, RAM, region, quantity, Brand_ID)
        return_to_menu()
    elif choice == '8':  # نمایش محصولات
        product_manager.show_products()
        return_to_menu()
    elif choice == '9':  # حذف محصول
        Product_ID = int(input("آی‌دی محصول را وارد کنید: "))
        product_manager.delete_product(Product_ID)
        return_to_menu()
    elif choice == "10":
        product_name = input("نام محصول را وارد کنید: """)
        product_manager.search_product(product_name)
        return_to_menu()
    elif choice == '11':  # نمایش محصولات با موجودی کم
        threshold = int(input("حداقل آستانه محصول را وارد کنید: "))
        product_manager.get_low_stock_products(threshold)
        return_to_menu()
    elif choice == '12':  # ثبت سفارش
        person = input("نام خریدار را وارد کنید")
        Product_ID = int(input("آی‌دی محصول را وارد کنید: "))
        quantity = int(input("تعداد محصول را وارد کنید: "))
        order_type = input("نوع سفارش (ورود/خروج) را وارد کنید (in/out): ")
        price = input("قیمت را وارد کنید")
        order_manager.add_order(person, Product_ID, quantity, price, order_type)
        return_to_menu()
    elif choice == '13':  # نمایش تاریخچه سفارش‌ها
        order_manager.show_orders_history()
        return_to_menu()
    elif choice == '14':  # حذف سفارش
        Order_ID = int(input("آی‌دی سفارش را وارد کنید: "))
        order_manager.delete_order(Order_ID)
        return_to_menu()
    elif choice == '15':  # اضافه کردن کاربر
        username = input("نام کاربری را وارد کنید: ")
        password = input("پسوورد را وارد کنید")
        role = input("نقش کاربر (admin یا employee) را وارد کنید: ")
        user_manager.add_user(username, password, role)
        return_to_menu()
    elif choice == '16':  # حذف کاربر
        User_ID = int(input("آی‌دی کاربر را وارد کنید: "))
        user_manager.delete_user(User_ID)
        return_to_menu()
    elif choice == "17":
        user_manager.show_all_users()
        return_to_menu()
    elif choice == '18':  # خروج
        print("\033[30;41m خروج \033[0m")
        return_to_menu()
        db.close()
        break

    else:
        print("لطفا یک گزینه معتبر انتخاب کنید")
