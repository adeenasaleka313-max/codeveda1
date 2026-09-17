import json 
import os

FILE_NAME = "tasks.json"


# Load tasks from the JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to the JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(tasks):
    title = input("Enter task: ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


# Delete a task
def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully!")
                return

            print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


# Mark a task as completed
def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID to mark as completed: "))

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST APPLICATION ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List!")
            break
        else:
            print("Invalid choice. Please try again.")


main()