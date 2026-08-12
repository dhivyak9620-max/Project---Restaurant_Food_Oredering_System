from database import connect_database
from cart import view_cart
from payment import make_payment

def place_order(customer, cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    total_amount = view_cart(cart)

    confirm = input("\nDo you want to place this order? (Y/N): ")
    if confirm.upper() != "Y":
        print("Order cancelled.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO orders
            (customer_id, order_status, total_amount)
            VALUES (%s, %s, %s)
        """, (customer[0], "PLACED", total_amount))

        order_id = cursor.lastrowid

        for item_id, item in cart.items():
            cursor.execute("""
                INSERT INTO order_items
                (order_id, item_id, quantity, price)
                VALUES (%s, %s, %s, %s)
            """, (
                order_id,
                item_id,
                item["quantity"],
                item["price"]
            ))

        connection.commit()

        print("\n========== ORDER PLACED ==========")
        print("Order ID:", order_id)
        print(f"Total Amount: ₹{total_amount:.2f}")

        cart.clear()
        make_payment(order_id, total_amount)

    except Exception as error:
        connection.rollback()
        print("Order could not be placed.")
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()

def order_history(customer):
    print("\n========== ORDER HISTORY ==========")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT order_id, order_date, order_status, total_amount
        FROM orders
        WHERE customer_id = %s
        ORDER BY order_date DESC
    """, (customer[0],))

    orders = cursor.fetchall()

    if not orders:
        print("No previous orders found.")
    else:
        for order_id, order_date, status, amount in orders:
            print(
                f"Order ID: {order_id} | "
                f"Date: {order_date} | "
                f"Status: {status} | "
                f"Amount: ₹{amount}"
            )

    cursor.close()
    connection.close()
