# 🍽️ Restaurant Food Ordering System

A console-based **Restaurant Food Ordering System** developed using **Python and MySQL**. The project demonstrates how a Python application can interact with a relational database to manage customers, menu items, shopping carts, orders, payments, and administrative operations.

## 📌 Project Description

This project simulates a real-world restaurant ordering workflow. Customers can register, log in, continue as guests, browse and search the menu, add items to a cart, update or remove items, place orders, make payments, and view order history.

The system also provides an admin workflow for managing menu items and availability, along with reporting functionality for sales and customer information.

## ✨ Features

### 👤 Customer
- Customer registration
- Customer login
- Guest access
- View complete menu
- View food by category
- Search food items
- Add items to cart
- Update cart quantity
- Remove items from cart
- Place orders
- View order history

### 🛠️ Admin
- Admin login
- View menu
- Add new menu items
- Update menu item availability

### 🛒 Cart Management
- Add food items
- Update quantities
- Remove items
- Calculate cart total

### 📦 Order Management
- Create customer orders
- Store order items
- Calculate total order amount
- Maintain order history
- Track order status

### 💳 Payment
- UPI payment option
- Cash payment option
- Card payment option
- Store payment details in MySQL

### 📊 Reports
- Total order count
- Total sales
- Customer count by customer type

## 🛠️ Technologies Used

- **Python 3**
- **MySQL**
- **mysql-connector-python**
- **SQL**
- Python modules and functions
- Relational database concepts

## 🗄️ Database Design

The MySQL database contains the following tables:

- `customers`
- `categories`
- `menu_items`
- `orders`
- `order_items`
- `payments`

The tables are connected using **primary keys and foreign keys** to maintain relationships between customers, menu items, orders, and payments.

## 📂 Project Structure

```text
Restaurant_Separate_files/
│
├── main.py
├── database.py
├── customer.py
├── menu.py
├── cart.py
├── order.py
├── payment.py
├── admin.py
├── reports.py
├── Restaurant_food_ordering_system.sql
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `main.py` | Main application and customer/admin menus |
| `database.py` | MySQL database connection |
| `customer.py` | Registration, login and guest access |
| `menu.py` | Menu viewing, category filtering and food search |
| `cart.py` | Cart operations |
| `order.py` | Order placement and order history |
| `payment.py` | Payment processing and recording |
| `admin.py` | Admin login and menu management |
| `reports.py` | Sales and customer reports |
| `Restaurant_food_ordering_system.sql` | Database, tables, sample data and relationships |

## ⚙️ Requirements

Before running the project, make sure you have:

1. **Python 3** installed
2. **MySQL Server** installed and running
3. **MySQL Connector for Python** installed

Install the connector using:

```bash
pip install mysql-connector-python
```

## 🗃️ Database Setup

### Step 1: Start MySQL

Make sure your MySQL server is running.

### Step 2: Run the SQL file

Open MySQL Workbench or MySQL command line and execute:

```text
Restaurant_food_ordering_system.sql
```

This creates the `restaurant_db` database, tables, relationships, and sample data.

### Step 3: Check database connection

Open `database.py` and make sure the connection details match your MySQL setup:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="restaurant_db"
)
```

> **Important:** Do not upload your real MySQL password to GitHub. Use a placeholder such as `YOUR_MYSQL_PASSWORD` before pushing the project to a public repository.

## ▶️ How to Run

Open the project folder in VS Code or Command Prompt/PowerShell.

Run:

```bash
python main.py
```

The application displays:

```text
======================================
    RESTAURANT FOOD ORDERING SYSTEM
======================================
1. Customer
2. Admin
3. Exit
```

Choose the required option and follow the menu prompts.

## 🔄 Application Workflow

```text
Start
  ↓
Customer / Admin
  ↓
Customer Registration / Login / Guest
  ↓
Browse / Search Menu
  ↓
Add Items to Cart
  ↓
Update / Remove Items
  ↓
Place Order
  ↓
Select Payment Method
  ↓
Payment Recorded
  ↓
View Order History
```

## 🎯 Key Learning Outcomes

This project provided hands-on experience with:

- Python programming
- MySQL database management
- SQL queries
- CRUD operations
- Primary and foreign keys
- Python-MySQL connectivity
- Modular programming
- Functions and modules
- Input validation
- Transaction handling
- Real-world application workflow design

## 👥 Team

**Team Member:** Mohanraj

## 🙏 Mentor

**Pushparaja**

## 🎓 Academy

**Techpanda Academy**

## 🚀 Future Enhancements

Possible improvements for future versions:

- Password-based authentication
- GUI or web interface
- Online payment gateway integration
- Order cancellation and refund management
- Real-time order status
- Advanced sales analytics
- Admin dashboard
- Environment variables for database credentials

## 📄 License

This project was created for **learning and educational purposes** as part of practical project development.
