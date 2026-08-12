from database import connect_database

def register_customer():
    print("\n========== CUSTOMER REGISTRATION ==========")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT customer_id FROM customers WHERE phone = %s", (phone,))
    if cursor.fetchone():
        print("Customer with this phone number already exists.")
        cursor.close()
        connection.close()
        return None

    query = """
        INSERT INTO customers
        (customer_name, phone, email, customer_type)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, phone, email or None, "REGISTERED"))
    connection.commit()
    customer_id = cursor.lastrowid

    print("Registration successful!")
    print("Customer ID:", customer_id)

    cursor.close()
    connection.close()
    return customer_id

def login_customer():
    print("\n========== CUSTOMER LOGIN ==========")
    phone = input("Enter your phone number: ")

    connection = connect_database()
    cursor = connection.cursor()

    query = """
        SELECT customer_id, customer_name, phone, email, customer_type
        FROM customers
        WHERE phone = %s AND customer_type = 'REGISTERED'
    """
    cursor.execute(query, (phone,))
    customer = cursor.fetchone()

    cursor.close()
    connection.close()

    if customer:
        print("Login successful!")
        print("Welcome,", customer[1])
        return customer

    print("Customer not found. Please register first.")
    return None

def continue_as_guest():
    print("\n========== GUEST CUSTOMER ==========")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    connection = connect_database()
    cursor = connection.cursor()

    query = """
        INSERT INTO customers (customer_name, phone, customer_type)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, phone, "GUEST"))
    connection.commit()
    customer_id = cursor.lastrowid

    cursor.close()
    connection.close()

    print("Guest access successful!")
    print("Welcome,", name)
    return (customer_id, name, phone, None, "GUEST")

if __name__ == "__main__":
    print("Customer module loaded successfully.")
