tasks = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Quit")

    choice = input("> ").strip()

    if choice == "1":
        new_task = input("Enter your task: ").strip()
        if new_task == "":
            print("No task entered.")
        else:
            tasks.append(new_task)
            print(f'"{new_task}" added to your list.')

    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("Your list is empty. Nothing to remove.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_input = input("Enter the number of the task to remove: ").strip()

            if task_input == "":
                print("No input received.")
            else:
                try:
                    task_num = int(task_input)
                    if task_num == 0:
                        print("Task number 0 does not exist.")
                    elif 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f'"{removed}" was removed.')
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        if choice == "":
            print("You pressed Enter without making a choice.")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")





    