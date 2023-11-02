class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{index}. {task.description} (Due: {task.due_date}, Priority: {task.priority}, Status: {status})")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            todo_list.add_task(description, due_date, priority)
            print("Task added successfully.")
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to update: "))
            new_description = input("Enter new task description: ")
            new_due_date = input("Enter new due date: ")
            new_priority = input("Enter new priority: ")
            todo_list.update_task(task_index, new_description, new_due_date, new_priority)
        elif choice == "5":
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
