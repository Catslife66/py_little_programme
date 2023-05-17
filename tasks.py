class Tasks:
    def __init__(self):
        self.todo_list = []
        self.done_list = []

    def add_todo(self, task, priority):
        new_task = {'task': task, 'priority': priority}
        self.todo_list.append(new_task)

    def done(self, task):
        for list_item in self.todo_list:
            if task in list_item['task']:
                self.todo_list.remove(list_item)
                self.done_list.append(task)


t = Tasks()
t.add_todo('check email', 3)
t.add_todo('concall', 1)


