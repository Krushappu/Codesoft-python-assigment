tasks = []

def add_task(task):
    """Add a task to the to-do list."""
    tasks.append(task)
    print(f"Task '{task}' added.")

class TodoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as complete.")
        else:
            print("Invalid task index.")

    def main(self):
        while True:
            print("\nTo-Do List Application")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    task_index = int(input("Enter the task number to mark as complete: "))
                    self.complete_task(task_index)
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.main()
