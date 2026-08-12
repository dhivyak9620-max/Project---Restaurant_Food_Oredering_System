from database import connect_database

def view_menu():
    print("\n========== RESTAURANT MENU ==========")

    connection = connect_database()
    cursor = connection.cursor()

    query = """
        SELECT m.item_id, m.item_name, m.price, c.category_name
        FROM menu_items m
        JOIN categories c ON m.category_id = c.category_id
        WHERE m.available = TRUE
        ORDER BY c.category_id, m.item_id
    """
    cursor.execute(query)
    items = cursor.fetchall()

    if not items:
        print("No menu items available.")
    else:
        current_category = None
        for item_id, item_name, price, category_name in items:
            if category_name != current_category:
                print(f"\n--- {category_name.upper()} ---")
                current_category = category_name
            print(f"{item_id}. {item_name} - ₹{price}")

    cursor.close()
    connection.close()

def view_menu_by_category():
    print("\n========== FOOD CATEGORIES ==========")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT category_id, category_name
        FROM categories
        ORDER BY category_id
    """)
    categories = cursor.fetchall()

    for category_id, category_name in categories:
        print(f"{category_id}. {category_name}")

    category_id = input("\nEnter category ID: ")

    cursor.execute("""
        SELECT item_id, item_name, price
        FROM menu_items
        WHERE category_id = %s AND available = TRUE
        ORDER BY item_id
    """, (category_id,))
    items = cursor.fetchall()

    print("\n========== FOOD ITEMS ==========")
    if not items:
        print("No food items found in this category.")
    else:
        for item_id, item_name, price in items:
            print(f"{item_id}. {item_name} - ₹{price}")

    cursor.close()
    connection.close()

def search_food():
    print("\n========== SEARCH FOOD ==========")
    search_term = input("Enter food name: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT item_id, item_name, price
        FROM menu_items
        WHERE item_name LIKE %s AND available = TRUE
        ORDER BY item_name
    """, ("%" + search_term + "%",))

    items = cursor.fetchall()

    if not items:
        print("No food items found.")
    else:
        print("\n========== SEARCH RESULTS ==========")
        for item_id, item_name, price in items:
            print(f"{item_id}. {item_name} - ₹{price}")

    cursor.close()
    connection.close()

def get_menu_item(item_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT item_id, item_name, price
        FROM menu_items
        WHERE item_id = %s AND available = TRUE
    """, (item_id,))
    item = cursor.fetchone()

    cursor.close()
    connection.close()
    return item

if __name__ == "__main__":
    view_menu()
