from database import connect_database

def make_payment(order_id, amount):
    print("\n========== PAYMENT ==========")
    print("1. UPI")
    print("2. Cash")
    print("3. Card")

    choice = input("Choose payment method: ")

    methods = {"1": "UPI", "2": "CASH", "3": "CARD"}
    if choice not in methods:
        print("Invalid payment method.")
        return False

    payment_method = methods[choice]

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO payments
        (order_id, payment_method, amount, payment_status)
        VALUES (%s, %s, %s, %s)
    """, (order_id, payment_method, amount, "PAID"))

    connection.commit()

    cursor.close()
    connection.close()

    print("Payment recorded successfully!")
    print("Payment Method:", payment_method)
    print(f"Amount Paid: ₹{amount:.2f}")
    return True
