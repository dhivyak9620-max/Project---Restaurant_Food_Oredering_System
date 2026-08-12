from database import connect_database

def sales_report():
    print("\n========== SALES REPORT ==========")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(order_id), COALESCE(SUM(total_amount), 0)
        FROM orders
        WHERE order_status = 'PLACED'
    """)

    order_count, total_sales = cursor.fetchone()

    print("Total Orders:", order_count)
    print(f"Total Sales: ₹{total_sales:.2f}")

    cursor.close()
    connection.close()

def customer_report():
    print("\n========== CUSTOMER REPORT ==========")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT customer_type, COUNT(customer_id)
        FROM customers
        GROUP BY customer_type
    """)

    for customer_type, count in cursor.fetchall():
        print(f"{customer_type} Customers: {count}")

    cursor.close()
    connection.close()
