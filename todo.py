# todo.py - Simple CLI To-Do List App

FILENAME = "tasks.txt"

def show_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("📭 No tasks found.")
        else:
            print("\n📋 Your To-Do List:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        open(FILENAME, "w").close()
        print("📁 Created new task file.")

def add_task():
    task = input("➕ Enter new task: ")
    with open(FILENAME, "a") as file:
        file.write(task + "\n")
    print("✅ Task added!")

def delete_task():
    show_tasks()
    try:
        num = int(input("❌ Enter task number to delete: "))
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            with open(FILENAME, "w") as file:
                file.writelines(tasks)
            print(f"🗑️ Removed: {removed.strip()}")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def main():
    while True:
        print("\n--- To-Do Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❓ Invalid choice.")

if __name__ == "__main__":
    main()
