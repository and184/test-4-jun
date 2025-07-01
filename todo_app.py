tasks = []

def show_tasks():
    print("\nВаши задачи:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Добавлено: {task}")

while True:
    command = input("\nВведите команду (add / list / exit): ").strip()
    
    if command == "add":
        task = input("Введите задачу: ")
        add_task(task)
    elif command == "list":
        show_tasks()
    elif command == "exit":
        print("Выход...")
        break
    else:
        print("Неизвестная команда.")
