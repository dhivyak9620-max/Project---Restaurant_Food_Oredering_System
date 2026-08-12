from database import connect_database
from menu import view_menu

def admin_login():
    print("\n========== ADMIN LOGIN ==========")
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        print("Admin login successful!")
        admin_menu()
    else:
        print("Invalid admin credentials.")

def add_category():
    print("\n========== ADD CATEGORY ==========")
    category_name = input("Enter category name: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO categories (category_name) VALUES (%s)",
        (category_name,)
    )
    connection.commit()

    print("Category added successfully.")
    cursor.close()
    connection.close()

def add_menu_item():
    print("\n========== ADD MENU ITEM ==========")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category_id, category_name
        FROM categories
        ORDER BY category_id
    """)

    for category_id, category_name in cursor.fetchall():
        print(f"{category_id}. {category_name}")

    try:
        category_id = int(input("Enter category ID: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid input.")
        cursor.close()
        connection.close()
        return

    item_name = input("Enter food name: ")

    cursor.execute("""
        INSERT INTO menu_items
        (item_name, category_id, price, available)
        VALUES (%s, %s, %s, %s)
    """, (item_name, category_id, price, True))

    connection.commit()
    print("Menu item added successfully.")

    cursor.close()
    connection.close()

def update_menu_availability():
    print("\n========== UPDATE FOOD AVAILABILITY ==========")
    view_menu()

    try:
        item_id = int(input("\nEnter item ID: "))
        available = int(input("Enter 1 for Available / 0 for Unavailable: "))
    except ValueError:
        print("Invalid input.")
        return

    if available not in (0, 1):
        print("Enter only 1 or 0.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE menu_items
        SET available = %s
        WHERE item_id = %s
    """, (available, item_id))

    connection.commit()

    print("Availability updated successfully." if cursor.rowcount else "Food item not found.")

    cursor.close()
    connection.close()

def admin_menu():
    while True:
        print("\n======================================")
        print("             ADMIN MENU")
        print("======================================")
        print("1. Add Category")
        print("2. Add Menu Item")
        print("3. Update Food Availability")
        print("4. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_category()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            update_menu_availability()
        elif choice == "4":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice.")
