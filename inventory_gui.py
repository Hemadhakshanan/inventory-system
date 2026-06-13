import tkinter as tk
from tkinter import messagebox, ttk

from inventory_operations import (
    add_product,
    stock_in,
    stock_out
)
from db_connection import connect_db

# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("Smart Inventory Management System")
root.geometry("900x650")
root.configure(bg="#f4f6f7")
# ---------------- FUNCTIONS ----------------

def show_alert_if_low_stock():
    conn = connect_db()

    cursor = conn.cursor()
    cursor.execute("SELECT product_name, quantity, minimum_stock FROM products")
    rows = cursor.fetchall()

    alerts = []

    for name, qty, min_stock in rows:
        if qty <= min_stock:
            alerts.append(f"⚠ {name} low stock ({qty})")

    if alerts:
        messagebox.showwarning("Low Stock Alert", "\n".join(alerts))

    cursor.close()
    conn.close()


def load_table():

    for row in tree.get_children():
        tree.delete(row)

    conn = connect_db()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

    cursor.close()
    conn.close()

    show_alert_if_low_stock()


def add_item():
    try:
        add_product(
            name_entry.get(),
            category_entry.get(),
            float(price_entry.get()),
            int(quantity_entry.get()),
            int(min_stock_entry.get())
        )
        messagebox.showinfo("Success", "Product Added Successfully!")
        load_table()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def stock_in_item():
    try:
        stock_in(int(id_entry.get()), int(stock_entry.get()))
        messagebox.showinfo("Success", "Stock IN Done!")
        load_table()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def stock_out_item():
    try:
        stock_out(int(id_entry.get()), int(stock_entry.get()))
        messagebox.showinfo("Success", "Stock OUT Done!")
        load_table()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- TITLE ----------------

tk.Label(
    root,
    text="SMART INVENTORY MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#f4f6f7",
    fg="#2c3e50"
).pack(pady=10)

# ---------------- INPUT SECTION ----------------

form = tk.Frame(root, bg="#f4f6f7")
form.pack(pady=10)

tk.Label(form, text="Name", bg="#f4f6f7").grid(row=0, column=0)
name_entry = tk.Entry(form)
name_entry.grid(row=0, column=1)

tk.Label(form, text="Category", bg="#f4f6f7").grid(row=0, column=2)
category_entry = tk.Entry(form)
category_entry.grid(row=0, column=3)

tk.Label(form, text="Price", bg="#f4f6f7").grid(row=1, column=0)
price_entry = tk.Entry(form)
price_entry.grid(row=1, column=1)

tk.Label(form, text="Quantity", bg="#f4f6f7").grid(row=1, column=2)
quantity_entry = tk.Entry(form)
quantity_entry.grid(row=1, column=3)

tk.Label(form, text="Min Stock", bg="#f4f6f7").grid(row=2, column=0)
min_stock_entry = tk.Entry(form)
min_stock_entry.grid(row=2, column=1)

tk.Button(form, text="Add Product", bg="#27ae60", fg="white",
          command=add_item).grid(row=2, column=3, padx=5)

# ---------------- STOCK SECTION ----------------

stock = tk.Frame(root, bg="#f4f6f7")
stock.pack(pady=10)

tk.Label(stock, text="Product ID", bg="#f4f6f7").grid(row=0, column=0)
id_entry = tk.Entry(stock)
id_entry.grid(row=0, column=1)

tk.Label(stock, text="Quantity", bg="#f4f6f7").grid(row=0, column=2)
stock_entry = tk.Entry(stock)
stock_entry.grid(row=0, column=3)

tk.Button(stock, text="Stock IN", bg="#f39c12", fg="white",
          command=stock_in_item).grid(row=1, column=1, pady=5)

tk.Button(stock, text="Stock OUT", bg="#e74c3c", fg="white",
          command=stock_out_item).grid(row=1, column=2, pady=5)

# ---------------- TABLE ----------------

tk.Label(root, text="INVENTORY DASHBOARD",
         font=("Arial", 14, "bold"),
         bg="#f4f6f7").pack(pady=10)

columns = ("ID", "Name", "Category", "Price", "Quantity", "Min Stock")

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.pack(pady=10)

tk.Button(root, text="Refresh Data", bg="#3498db", fg="white",
          command=load_table).pack(pady=5)

# ---------------- INIT ----------------

load_table()

root.mainloop()