import sqlite3
import sys

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create the employees table (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary INTEGER NOT NULL
)
''')
conn.commit()

# Function to add a new employee
def add_employee():
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = int(input("Enter employee salary: "))
    
    cursor.execute('''
    INSERT INTO employees (name, position, salary)
    VALUES (?, ?, ?)
    ''', (name, position, salary))
    
    conn.commit()
    print("Employee added successfully.")

# Function to view all employees
def view_all_employees():
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    
    if not employees:
        print("No employees found.")
    else:
        print("Employees List:")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Position: {emp[2]}, Salary: {emp[3]}")

# Function to update an employee's details
def update_employee():
    emp_id = int(input("Enter employee ID to update: "))
    name = input("Enter new name (leave blank to keep unchanged): ")
    position = input("Enter new position (leave blank to keep unchanged): ")
    salary = input("Enter new salary (leave blank to keep unchanged): ")

    # Construct the update query
    update_query = "UPDATE employees SET"
    update_values = []

    if name:
        update_query += " name = ?,"
        update_values.append(name)
    if position:
        update_query += " position = ?,"
        update_values.append(position)
    if salary:
        update_query += " salary = ?,"
        update_values.append(int(salary))
    
    # Remove the trailing comma
    update_query = update_query.rstrip(',')
    update_query += " WHERE emp_id = ?"
    update_values.append(emp_id)

    cursor.execute(update_query, tuple(update_values))
    conn.commit()
    print(f"Employee ID {emp_id} updated successfully.")

# Function to delete an employee
def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    
    cursor.execute('DELETE FROM employees WHERE emp_id = ?', (emp_id,))
    conn.commit()
    print(f"Employee ID {emp_id} deleted successfully.")

# Function to exit the program
def exit_program():
    print("Exiting the program...")
    conn.close()  # Close the database connection
    sys.exit()  # Exit the program

# Menu-driven interface
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
