import csv
import os
from datetime import datetime
from collections import defaultdict

# File to store expense data
EXPENSE_FILE = "expenses.csv"

# Default categories
CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"]

# Ensure the CSV file exists
if not os.path.exists(EXPENSE_FILE):
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        print("Select a category:")
        for i, category in enumerate(CATEGORIES, 1):
            print(f"{i}. {category}")
        print(f"{len(CATEGORIES) + 1}. Add a new category")

        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(CATEGORIES):
            category = CATEGORIES[choice - 1]
        elif choice == len(CATEGORIES) + 1:
            category = input("Enter new category: ").strip()
            CATEGORIES.append(category)
        else:
            print("Invalid choice!")
            return
        
        description = input("Enter a brief description: ").strip()
        date = datetime.today().strftime("%Y-%m-%d")

        # Save to CSV file
        with open(EXPENSE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])

        print("Expense added successfully!\n")
    
    except ValueError:
        print("Invalid input! Please enter numeric values for amount.")

# Function to display all expenses
def view_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return
        
        print("\nDate        | Amount  | Category         | Description")
        print("-" * 50)
        for row in expenses:
            print(f"{row[0]} | {row[1]:<7} | {row[2]:<15} | {row[3]}")
        print()
    
    except FileNotFoundError:
        print("No expenses found. Start adding expenses first.")

# Function to show monthly summary
def monthly_summary():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return
        
        monthly_expenses = defaultdict(float)
        for row in expenses:
            date, amount = row[0], float(row[1])
            month = date[:7]  # Extract YYYY-MM
            monthly_expenses[month] += amount
        
        print("\nMonthly Summary")
        print("-" * 20)
        for month, total in monthly_expenses.items():
            print(f"{month}: ${total:.2f}")
        print()
    
    except FileNotFoundError:
        print("No expenses found.")

# Function to show category-wise expenditure
def category_summary():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

        if not expenses:
            print("No expenses recorded yet.")
            return

        category_expenses = defaultdict(float)
        for row in expenses:
            category, amount = row[2], float(row[1])
            category_expenses[category] += amount
        
        print("\nCategory-wise Summary")
        print("-" * 30)
        for category, total in category_expenses.items():
            print(f"{category}: ${total:.2f}")
        print()
    
    except FileNotFoundError:
        print("No expenses found.")

# Main menu function
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
