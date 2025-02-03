FridgeApp
FridgeApp is a simple Python-based application for managing a fridge inventory. It allows users to track items in their fridge, their quantities, and their expiry dates.

Features
Track items in your fridge (name, quantity, expiry date)
View the current inventory
Update quantities or remove items
Simple database to store fridge data
Requirements
Python 3.x
SQLite (for the fridge inventory database)

Installation
Clone the repository:
git clone https://github.com/jeffrey3107/fridgeApp.git
cd fridgeApp

Install the required Python packages:
pip install -r requirements.txt


Set up the database:
The app uses a simple SQLite database (fridge_inventory.db) that is automatically created when you run the app.

Usage
Run the app:
python fridge.py
Follow the prompts to add, update, or remove items from your fridge.
