from menu import view_menu, get_menu_item

def add_to_cart(cart):
    view_menu()

    try:
        item_id = int(input("\nEnter item ID: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    item = get_menu_item(item_id)
    if not item:
        print("Invalid or unavailable item.")
        return

    item_id, item_name, price = item
    price = float(price)

    if item_id in cart:
        cart[item_id]["quantity"] += quantity
    else:
        cart[item_id] = {
            "item_name": item_name,
            "price": price,
            "quantity": quantity
        }

    print(f"{quantity} x {item_name} added to cart.")

def view_cart(cart):
    print("\n========== YOUR CART ==========")

    if not cart:
        print("Your cart is empty.")
        return 0

    total = 0
    print("\nID   Item                 Qty    Price    Total")
    print("-" * 55)

    for item_id, item in cart.items():
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(
            f"{item_id:<4} {item['item_name']:<20} "
            f"{item['quantity']:<6} ₹{item['price']:<7.2f} "
            f"₹{item_total:.2f}"
        )

    print("-" * 55)
    print(f"Cart Total: ₹{total:.2f}")
    return total

def update_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return

    view_cart(cart)

    try:
        item_id = int(input("\nEnter item ID to update: "))
        quantity = int(input("Enter new quantity: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if item_id not in cart:
        print("Item is not present in cart.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    cart[item_id]["quantity"] = quantity
    print("Cart updated successfully.")

def remove_from_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return

    view_cart(cart)

    try:
        item_id = int(input("\nEnter item ID to remove: "))
    except ValueError:
        print("Please enter a valid item ID.")
        return

    if item_id in cart:
        removed = cart.pop(item_id)
        print(f"{removed['item_name']} removed from cart.")
    else:
        print("Item is not present in cart.")
