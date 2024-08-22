import json

# File for storing employee data
DATA_FILE = "employees.json"

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Register a new employee
def register_employee(employees):
    employee_id = input("Enter employee ID: ")
    if employee_id in employees:
        print("An employee with this ID is already registered.")
        return

    name = input("Enter employee name: ")
    position = input("Enter employee position: ")

    employees[employee_id] = {
        "name": name,
        "position": position
    }
    save_data(employees)
    print(f"Employee {name} has been successfully registered.")

# View all registered employees
def view_employees(employees):
    if not employees:
        print("No employees registered.")
        return

    for employee_id, details in employees.items():
        print(f"ID: {employee_id}, Name: {details['name']}, Position: {details['position']}")

# Update employee information
def update_employee(employees):
    employee_id = input("Enter the ID of the employee you want to update: ")
    if employee_id not in employees:
        print("Employee with this ID not found.")
        return

    name = input("Enter new employee name (leave blank to keep current): ")
    position = input("Enter new employee position (leave blank to keep current): ")

    if name:
        employees[employee_id]['name'] = name
    if position:
        employees[employee_id]['position'] = position

    save_data(employees)
    print(f"Employee information for ID {employee_id} has been updated.")

# Delete an employee
def delete_employee(employees):
    employee_id = input("Enter the ID of the employee you want to delete: ")
    if employee_id not in employees:
        print("Employee with this ID not found.")
        return

    del employees[employee_id]
    save_data(employees)
    print(f"Employee {employee_id} has been successfully deleted.")

# Main menu of the program
def main():
    employees = load_data()

    while True:
        print("\n--- Employee Registration System ---")
        print("1. Register a new employee")
        print("2. View all employees")
        print("3. Update employee information")
        print("4. Delete an employee")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            update_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
