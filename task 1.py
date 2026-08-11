# To-Do List Application

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter a new task: ").strip()

        if task:
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    # Update Task
    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                number = int(input("Enter task number to update: "))

                if 1 <= number <= len(tasks):
                    new_task = input("Enter the updated task: ").strip()

                    if new_task:
                        tasks[number - 1] = new_task
                        print("Task updated successfully!")
                    else:
                        print("Task cannot be empty.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print(f"Task '{deleted_task}' deleted successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please select 1-5.")
