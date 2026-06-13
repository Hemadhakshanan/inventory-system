# Smart Inventory Management System

A comprehensive Python-based inventory management application with a graphical user interface built using Tkinter and MySQL database integration.

## 📋 Overview

The Smart Inventory Management System is a desktop application designed to efficiently manage product inventory, track stock levels, and monitor low-stock alerts. It provides an intuitive graphical interface for adding products, managing stock levels, and viewing inventory data in real-time.

## ✨ Features

- **Product Management**: Add, view, and manage product information
- **Stock Tracking**: Monitor product quantities and stock levels
- **Stock Operations**: 
  - Stock IN: Add products to inventory
  - Stock OUT: Remove products from inventory
- **Low Stock Alerts**: Automatic warnings when stock falls below minimum threshold
- **Real-time Dashboard**: View complete inventory data in a structured table format
- **Database Integration**: MySQL backend for persistent data storage
- **User-Friendly GUI**: Intuitive Tkinter-based interface for easy navigation

## 🛠️ Tech Stack

- **Frontend**: Python Tkinter (GUI Framework)
- **Backend**: Python
- **Database**: MySQL
- **Database Connector**: mysql-connector-python

## 📁 Project Structure

```
inventory-management-system/
├── main.py                    # Application entry point
├── inventory_gui.py           # GUI components and interface
├── inventory_operations.py    # Core inventory operations (add, stock in/out)
├── db_connection.py           # Database connection handler
├── config.py                  # Configuration settings
├── report_generator.py        # Report generation functionality
├── README.md                  # Project documentation
└── exports/
    └── screenshots/           # Application screenshots
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- MySQL Server
- pip (Python Package Manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hemadhakshanan/inventory-system.git
   cd inventory-system
   ```

2. **Install dependencies**
   ```bash
   pip install mysql-connector-python
   ```

3. **Configure Database**
   - Edit `config.py` with your MySQL credentials:
   ```python
   DB_CONFIG = {
       "host": "localhost",
       "user": "your_username",
       "password": "your_password",
       "database": "inventory_db"
   }
   ```

4. **Create Database Schema**
   - Create a MySQL database named `inventory_db`
   - Create the `products` table with the following schema:
   ```sql
   CREATE TABLE products (
       id INT AUTO_INCREMENT PRIMARY KEY,
       product_name VARCHAR(100) NOT NULL,
       category VARCHAR(50),
       price DECIMAL(10, 2),
       quantity INT,
       minimum_stock INT
   );
   ```

## 💻 Usage

### Running the Application

```bash
python main.py
```

or directly

```bash
python inventory_gui.py
```

### Using the Application

1. **Add Product**: Fill in product details (Name, Category, Price, Quantity, Min Stock) and click "Add Product"
2. **View Inventory**: See all products in the dashboard table
3. **Stock Operations**: 
   - Enter Product ID and quantity, then click "Stock IN" to add stock
   - Enter Product ID and quantity, then click "Stock OUT" to reduce stock
4. **Refresh Data**: Click "Refresh Data" to update the inventory display
5. **Low Stock Alerts**: The system automatically alerts when stock falls below the minimum threshold

## 🔧 Building Executable

To create a standalone executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed inventory_gui.py
```

The executable will be created in the `dist/` folder.

## 📊 Database Operations

### inventory_operations.py

Contains core functions:
- `add_product()`: Add new product to inventory
- `stock_in()`: Increase stock quantity
- `stock_out()`: Decrease stock quantity

### db_connection.py

Manages database connectivity:
- `connect_db()`: Establishes MySQL connection using credentials from config.py

## ⚙️ Configuration

Edit `config.py` to customize:
- Database hostname
- Database username
- Database password
- Database name

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "inventory_db"
}
```

## 🎨 UI Features

- **Clean Interface**: Modern, organized layout with clear sections
- **Color-Coded Buttons**: 
  - Green: Add Product
  - Orange: Stock IN
  - Red: Stock OUT
  - Blue: Refresh Data
- **Real-time Alerts**: Warning messages for low stock items
- **Responsive Table**: Displays all inventory data with proper formatting

## 🐛 Troubleshooting

### "Connection refused" Error
- Ensure MySQL Server is running
- Check database credentials in `config.py`
- Verify database and tables exist

### "No module named 'mysql.connector'"
- Install mysql-connector-python: `pip install mysql-connector-python`

### GUI doesn't appear
- Ensure Tkinter is installed: `pip install tk`
- Try running with: `python -m tkinter` to verify Tkinter installation

## 📝 Future Enhancements

- Product search and filtering
- Advanced reporting features
- User authentication and roles
- Barcode scanning integration
- Inventory history tracking
- Multi-location support
- Export to Excel/PDF reports

## 👨‍💻 Author

**Hemadhakshan**

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

For questions or support, please reach out to the project maintainer.

---

**Last Updated**: 2026-06-13
**Version**: 1.0.0
