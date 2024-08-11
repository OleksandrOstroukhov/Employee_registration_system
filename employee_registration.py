import json

# Файл для хранения данных сотрудников
DATA_FILE = "employees.json"

# Загрузка данных из файла
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Сохранение данных в файл
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Регистрация нового сотрудника
def register_employee(employees):
    employee_id = input("Введите ID сотрудника: ")
    if employee_id in employees:
        print("Сотрудник с таким ID уже зарегистрирован.")
        return

    name = input("Введите имя сотрудника: ")
    position = input("Введите должность сотрудника: ")

    employees[employee_id] = {
        "name": name,
        "position": position
    }
    save_data(employees)
    print(f"Сотрудник {name} успешно зарегистрирован.")

# Просмотр всех зарегистрированных сотрудников
def view_employees(employees):
    if not employees:
        print("Нет зарегистрированных сотрудников.")
        return

    for employee_id, details in employees.items():
        print(f"ID: {employee_id}, Имя: {details['name']}, Должность: {details['position']}")

# Обновление информации о сотруднике
def update_employee(employees):
    employee_id = input("Введите ID сотрудника, которого нужно обновить: ")
    if employee_id not in employees:
        print("Сотрудник с таким ID не найден.")
        return

    name = input("Введите новое имя сотрудника (оставьте пустым, чтобы не изменять): ")
    position = input("Введите новую должность сотрудника (оставьте пустым, чтобы не изменять): ")

    if name:
        employees[employee_id]['name'] = name
    if position:
        employees[employee_id]['position'] = position

    save_data(employees)
    print(f"Информация о сотруднике {employee_id} обновлена.")

# Удаление сотрудника
def delete_employee(employees):
    employee_id = input("Введите ID сотрудника, которого нужно удалить: ")
    if employee_id not in employees:
        print("Сотрудник с таким ID не найден.")
        return

    del employees[employee_id]
    save_data(employees)
    print(f"Сотрудник {employee_id} успешно удален.")

# Главное меню программы
def main():
    employees = load_data()

    while True:
        print("\n--- Система регистрации сотрудников ---")
        print("1. Зарегистрировать нового сотрудника")
        print("2. Просмотреть всех сотрудников")
        print("3. Обновить информацию о сотруднике")
        print("4. Удалить сотрудника")
        print("5. Выход")

        choice = input("Выберите действие: ")

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
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
