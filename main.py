from task import Task  # Importing the Task class from an external module


class ToDoList:
    # Class attributes (shared across all instances, should be instance variables instead)
    done = False  # Tracks whether the to-do list session should end
    tasks = []  # Stores the list of tasks

    def addTask(self):
        """Prompts the user to add a task with a name, due date, and priority."""
        task_name = input("What is the task? ")  # Get task name from user
        due_date = input("How many days do you have to complete this task? ")  # Get due date

        # Ensure priority is a valid number between 1 and 10
        priority = None
        while True:
            try:
                priority = int(input("How important is it on a scale of 1 - 10? "))
                if 1 <= priority <= 10:
                    break  # Exit loop if input is valid
                else:
                    print("Priority must be between 1 and 10.")  # Validation message
            except ValueError:
                print("Please enter a valid number.")  # Handles non-numeric input

        # Create a new Task object and add it to the task list
        new_task = Task(task_name, due_date, priority)
        self.tasks.append(new_task)
        print("Task added!")

    def printByPriority(self):
        """Prints tasks sorted by priority (highest first)."""
        sorted_tasks = sorted(self.tasks, key=lambda task: task.priority, reverse=True)
        for i, task in enumerate(sorted_tasks, 1):
            print(f"{i}. {task.name}")  # Prints task number and name

    def printByDueDate(self):
        """Prints tasks sorted by due date (earliest first)."""
        sorted_tasks = sorted(self.tasks, key=lambda task: task.due, reverse=False)
        for i, task in enumerate(sorted_tasks, 1):
            print(f"{i}. {task.name}")  # Prints task number and name

    def run(self):
        """Main loop for managing the to-do list."""
        while not self.done:
            addTask = input("Would you like to add a task? ").strip().lower()  # Get user input

            if addTask == 'yes':
                self.addTask()  # Calls the addTask function

            elif addTask == 'no':
                # If no tasks are available, notify the user
                if len(self.tasks) == 0:
                    print("\nYou have no tasks to complete.")

                # If only one task is available, notify the user
                elif len(self.tasks) == 1:
                    print("\nYou have one task to complete!")
                    for task in self.tasks:
                        print(task.name)

                    self.done = True  # End the loop

                else:
                    # Prompt user for sorting preference
                    order = input("\nWould you like to see your tasks by due date or priority?: ").strip().lower()

                    if order == "due date":
                        self.printByDueDate()
                        self.done = True

                    elif order == "priority":
                        self.printByPriority()
                        self.done = True

                    else:
                        print("Invalid input")  # Handles incorrect input

            else:
                print("Invalid input")  # Handles unexpected user responses


# Create a ToDoList instance and start the application
toDoList = ToDoList()
toDoList.run()
