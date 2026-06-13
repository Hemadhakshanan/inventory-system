from db_connection import connect_db

# ------------------ ADD PRODUCT ------------------

def add_product(name, category, price, quantity, minimum_stock):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO products (product_name, category, price, quantity, minimum_stock)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, category, price, quantity, minimum_stock)

    cursor.execute(query, values)
    conn.commit()

    print("✅ Product added successfully!")

    cursor.close()
    conn.close()


# ------------------ VIEW PRODUCTS ------------------

def view_products():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    print("\n📦 INVENTORY LIST:\n")

    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Category: {row[2]} | Price: {row[3]} | Qty: {row[4]} | Min Stock: {row[5]}")

    cursor.close()
    conn.close()


# ------------------ UPDATE PRODUCT ------------------

def update_product(product_id, price, quantity):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    UPDATE products
    SET price = %s,
        quantity = %s
    WHERE product_id = %s
    """

    cursor.execute(query, (price, quantity, product_id))
    conn.commit()

    print("✅ Product updated successfully!")

    cursor.close()
    conn.close()


# ------------------ DELETE PRODUCT ------------------

def delete_product(product_id):

    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM products WHERE product_id = %s"

    cursor.execute(query, (product_id,))
    conn.commit()

    print("🗑 Product deleted successfully!")

    cursor.close()
    conn.close()


# ------------------ STOCK IN ------------------

def stock_in(product_id, quantity):

    conn = connect_db()
    cursor = conn.cursor()

    # Increase stock
    query1 = """
    UPDATE products
    SET quantity = quantity + %s
    WHERE product_id = %s
    """
    cursor.execute(query1, (quantity, product_id))

    # Log transaction
    query2 = """
    INSERT INTO transactions (product_id, transaction_type, quantity)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query2, (product_id, "STOCK_IN", quantity))

    conn.commit()

    print(f"✅ Stock IN successful (+{quantity})")

    cursor.close()
    conn.close()


# ------------------ STOCK OUT ------------------

def stock_out(product_id, quantity):

    conn = connect_db()
    cursor = conn.cursor()

    # Check current stock
    cursor.execute("SELECT quantity FROM products WHERE product_id = %s", (product_id,))
    result = cursor.fetchone()

    if not result:
        print("❌ Product not found")
        return

    current_stock = result[0]

    if quantity > current_stock:
        print("❌ Not enough stock available")
        return

    # Decrease stock
    query1 = """
    UPDATE products
    SET quantity = quantity - %s
    WHERE product_id = %s
    """
    cursor.execute(query1, (quantity, product_id))

    # Log transaction
    query2 = """
    INSERT INTO transactions (product_id, transaction_type, quantity)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query2, (product_id, "STOCK_OUT", quantity))

    conn.commit()

    print(f"✅ Stock OUT successful (-{quantity})")

    cursor.close()
    conn.close()