from customer import register_customer, login_customer, continue_as_guest
from menu import view_menu, view_menu_by_category, search_food
from cart import add_to_cart, view_cart, update_cart, remove_from_cart
from order import place_order, order_history
from admin import admin_login


def customer_menu(customer):
    cart = {}

    while True:
        print("\n======================================")
        print("          CUSTOMER MENU")
        print("======================================")
        print("1. View Menu")
        print("2. View Food by Category")
        print("3. Search Food")
        print("4. Add Food to Cart")
        print("5. View Cart")
        print("6. Update Cart")
        print("7. Remove Item from Cart")
        print("8. Place Order")
        print("9. Order History")
        print("10. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_menu()
        elif choice == "2":
            view_menu_by_category()
        elif choice == "3":
            search_food()
        elif choice == "4":
            add_to_cart(cart)
        elif choice == "5":
            view_cart(cart)
        elif choice == "6":
            update_cart(cart)
        elif choice == "7":
            remove_from_cart(cart)
        elif choice == "8":
            place_order(customer, cart)
        elif choice == "9":
            order_history(customer)
        elif choice == "10":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n======================================")
        print("    RESTAURANT FOOD ORDERING SYSTEM")
        print("======================================")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n========== CUSTOMER ==========")
            print("1. Register")
            print("2. Login")
            print("3. Continue as Guest")
            print("4. Back")

            customer_choice = input("\nEnter your choice: ")

            if customer_choice == "1":
                register_customer()
            elif customer_choice == "2":
                customer = login_customer()
                if customer:
                    customer_menu(customer)
            elif customer_choice == "3":
                customer = continue_as_guest()
                if customer:
                    customer_menu(customer)
            elif customer_choice == "4":
                continue
            else:
                print("Invalid choice.")

        elif choice == "2":
            admin_login()

        elif choice == "3":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
