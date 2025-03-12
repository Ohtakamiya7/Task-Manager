class Task:
  name = None
  due = None
  priority = None
  
  def __init__(self, name, due_date, priority):
    self.name = name
    self.due = due_date
    self.priority = priority