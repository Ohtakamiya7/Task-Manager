from task import Task


class ToDoList:
  done = False
  tasks = []

  def addTask(self):
    task_name = input("What is the task? ")
    due_date = input("How many days do you have to complete this task? ")
    priority = None
    while True:
      try:
        priority = int(input("How important is it on a scale of 1 - 10? "))
        if 1 <= priority <= 10:
          break
        else:
          print("Priority must be between 1 and 10.")
      except ValueError:
        print("Please enter a valid number.")

    new_task = Task(task_name, due_date, priority)
    self.tasks.append(new_task)
    print("Task added!")

  def printByPriority(self):
    sorted_tasks = sorted(self.tasks,
                          key=lambda task: task.priority,
                          reverse=True)
    for i, task in enumerate(sorted_tasks, 1):
      print({i}, task.name)

  def printByDueDate(self):
    sorted_tasks = sorted(self.tasks, key=lambda task: task.due, reverse=False)
    for i, task in enumerate(sorted_tasks, 1):
      print({i}, ".", task.name)

  def run(self):
    while (not self.done):
      addTask = input("Would you like to add a task? (yes/no)")

      if addTask.lower() == 'yes':
        self.addTask()

      elif addTask.lower() == 'no':
        if len(self.tasks) == 0:
          print("\nYou have no tasks to complete.")

        elif len(self.tasks) == 1:
          print("\nYou have one task to complete!")
          for task in self.tasks:
            print(task.name)

          self.done = True

        else:
          order = input(
              "\nWould you like to see your tasks by due date or priority?: ")

          if (order.lower() == "due date"):
            self.printByDueDate()
            self.done = True

          elif (order.lower() == "priority"):
            self.printByPriority()
            self.done = True

          else:
            print("Invalid input")

      else:
        print("Invalid input")


toDoList = ToDoList()
toDoList.run()
