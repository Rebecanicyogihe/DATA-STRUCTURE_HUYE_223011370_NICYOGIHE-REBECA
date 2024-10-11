from collections import deque

# List of tasks with TaskID, TaskName, and ProjectName
tasks = [
    {"TaskID": 201, "TaskName": "Design homepage", "ProjectName": "Website Redesign"},
    {"TaskID": 202, "TaskName": "Develop user authentication", "ProjectName": "Mobile App Development"},
    {"TaskID": 203, "TaskName": "Set up payment gateway", "ProjectName": "E-commerce Platform"},
    {"TaskID": 204, "TaskName": "Create ad creatives", "ProjectName": "Social Media Campaign"},
    {"TaskID": 205, "TaskName": "Optimize blog SEO", "ProjectName": "SEO Optimization"},
    {"TaskID": 206, "TaskName": "Develop user dashboard", "ProjectName": "Custom CRM System"},
    {"TaskID": 207, "TaskName": "Design company logo", "ProjectName": "Logo Design"},
    {"TaskID": 208, "TaskName": "Configure cloud servers", "ProjectName": "Cloud Infrastructure Setup"},
    {"TaskID": 209, "TaskName": "Create data visualization", "ProjectName": "Data Analysis Dashboard"},
    {"TaskID": 210, "TaskName": "Edit promo video", "ProjectName": "Video Editing"},
    {"TaskID": 211, "TaskName": "Design social media ads", "ProjectName": "Social Media Ads"},
    {"TaskID": 212, "TaskName": "Audit network security", "ProjectName": "Cybersecurity Audit"},
    {"TaskID": 213, "TaskName": "Design landing page", "ProjectName": "Product Landing Page"},
    {"TaskID": 214, "TaskName": "Develop chatbot interface", "ProjectName": "AI Chatbot Development"},
    {"TaskID": 215, "TaskName": "Record podcast episode", "ProjectName": "Podcast Production"},
    {"TaskID": 216, "TaskName": "Integrate blockchain API", "ProjectName": "Blockchain Integration"},
    {"TaskID": 217, "TaskName": "Migrate database to cloud", "ProjectName": "Database Migration"},
    {"TaskID": 218, "TaskName": "Develop character animations", "ProjectName": "Mobile Game Development"},
    {"TaskID": 219, "TaskName": "Set up online course structure", "ProjectName": "Online Course Platform"},
    {"TaskID": 220, "TaskName": "Create AR environment", "ProjectName": "Augmented Reality App"}
]

# Stack for undoing task assignments
undo_stack = []

# Queue for pending tasks
task_queue = deque()

# Function to add a task to the queue
def add_task(task_id):
    for task in tasks:
        if task["TaskID"] == task_id:
            task_queue.append({"TaskID": task_id, "TaskName": task["TaskName"], "ProjectName": task["ProjectName"]})
            print(f"Task '{task['TaskName']}' added for project '{task['ProjectName']}'.")
            return
    print("Invalid Task ID. Please choose a valid task from the list.")

# Function to assign and process the next task in the queue
def assign_task():
    if task_queue:
        next_task = task_queue.popleft()
        undo_stack.append(next_task)
        print(f"Task '{next_task['TaskName']}' for project '{next_task['ProjectName']}' has been assigned.")
    else:
        print("No tasks to process.")

# Function to undo the last task assignment
def undo_last_assignment():
    if undo_stack:
        last_task = undo_stack.pop()
        task_queue.appendleft(last_task)
        print(f"Undo successful: Task '{last_task['TaskName']}' has been re-added for project '{last_task['ProjectName']}'.")
    else:
        print("No tasks to undo.")

# Function to view pending tasks
def view_pending_tasks():
    if task_queue:
        print("\nPending Tasks:")
        for task in task_queue:
            print(f"Task: '{task['TaskName']}' for project '{task['ProjectName']}'.")
    else:
        print("No pending tasks at the moment.")

# Main menu for interaction
def task_manager():
    while True:
        print("\nOptions:")
        print("1. Display All Tasks")
        print("2. Add Task by ID")
        print("3. Assign and Process Next Task")
        print("4. Undo Last Task Assignment")
        print("5. View Pending Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            print("\nAvailable Tasks:")
            for task in tasks:
                print(f"Task ID: {task['TaskID']}, Task: {task['TaskName']}, Project: {task['ProjectName']}")
        elif choice == '2':
            try:
                task_id = int(input("Enter Task ID to add: "))
                add_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            assign_task()
        elif choice == '4':
            undo_last_assignment()
        elif choice == '5':
            view_pending_tasks()
        elif choice == '6':
            print("Exiting task manager system.")
            break
        else:
            print("Invalid choice, please select a valid option.")

# Run the task manager system
task_manager()
