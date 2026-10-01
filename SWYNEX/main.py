from task_manager import add_task, view_tasks, delete_task


def main():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_task()

            elif choice == 2:
                view_tasks()

            elif choice == 3:
                delete_task()

            elif choice == 4:
                print("Thank you for using Task Manager!")
                break

            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
