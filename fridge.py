# write a python code for an app that lists the inventory in a fridge
import sqlite3
from datetime import datetime

# Database connection
conn = sqlite3.connect("fridge_inventory.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    expiry_date TEXT
                )''')
conn.commit()

def list_inventory():
    """Displays all items in the fridge"""
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    
    if not items:
        print("\nThe fridge is empty!\n")
    else:
        print("\n📦 Fridge Inventory 📦")
        print("-" * 40)
        for item in items:
            print(f"🛒 {item[1]} - {item[2]} units (Expires on: {item[3]})")
        print("-" * 40)

def add_item():
    """Adds a new item to the fridge"""
    item_name = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: "))
    expiry_date = input("Enter expiry date (YYYY-MM-DD) or leave blank: ").strip()

    if expiry_date == "":
        expiry_date = "No Expiry"
    
    cursor.execute("INSERT INTO inventory (item_name, quantity, expiry_date) VALUES (?, ?, ?)",
                   (item_name, quantity, expiry_date))
    conn.commit()
    print(f"✅ {item_name} added to the fridge!")

def remove_item():
    """Removes an item from the fridge"""
    list_inventory()
    item_name = input("Enter the item name to remove: ").strip()
    
    cursor.execute("DELETE FROM inventory WHERE item_name = ?", (item_name,))
    conn.commit()
    print(f"❌ {item_name} removed from the fridge!")

def check_item():
    """Checks if an item is in the fridge"""
    item_name = input("Enter the item name to check: ").strip()
    
    cursor.execute("SELECT * FROM inventory WHERE item_name = ?", (item_name,))
    item = cursor.fetchone()
    
    if item:
        print(f"✅ {item_name} is in the fridge! {item[2]} units left, Expiry Date: {item[3]}")
    else:
        print(f"⚠️ {item_name} is not in the fridge!")

def main():
    """Main function for user interaction"""
    while True:
        print("\n==== Fridge Inventory Management ====")
        print("1️⃣ List Inventory")
        print("2️⃣ Add Item")
        print("3️⃣ Remove Item")
        print("4️⃣ Check Item")
        print("5️⃣ Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            list_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            check_item()
        elif choice == "5":
            print("👋 Exiting the fridge inventory app. Stay fresh!")
            conn.close()
            break
        else:
            print("⚠️ Invalid option. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
