class Task:
    def __init__(self, description, due_date=None, priority='Medium', category='General', status='Pending'):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.status = status

    def __str__(self):
        return f"{self.description} | Due: {self.due_date} | Priority: {self.priority} | Category: {self.category} | Status: {self.status}"
def add_task(task_list):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low, Medium, High): ")
    category = input("Enter category: ")
    task = Task(description, due_date, priority, category)
    task_list.append(task)
    print("Task added successfully!")

def view_tasks(task_list):
    if not task_list:
        print("No tasks available.")
        return
    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task}")

def update_task(task_list):
    view_tasks(task_list)
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(task_list):
        task = task_list[task_number]
        task.description = input(f"Enter new description (current: {task.description}): ")
        task.due_date = input(f"Enter new due date (current: {task.due_date}): ")
        task.priority = input(f"Enter new priority (current: {task.priority}): ")
        task.category = input(f"Enter new category (current: {task.category}): ")
        task.status = input(f"Enter new status (current: {task.status}): ")
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def delete_task(task_list):
    view_tasks(task_list)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(task_list):
        del task_list[task_number]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")
def main():
    task_list = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            update_task(task_list)
        elif choice == '4':
            delete_task(task_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
