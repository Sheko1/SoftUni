from todo_list.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def __find_task(self, name: str):
        for i in range(len(self.tasks)):
            if self.tasks[i].name == name:
                return i

    def add_task(self, task: Task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        completed_task = self.__find_task(task_name)

        if completed_task is None:
            return f"Could not find task with the name {task_name}"

        self.tasks[completed_task].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        before_count_task = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {abs(len(self.tasks) - before_count_task)} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"

        for task in self.tasks:
            result += f"{task.details()}\n"

        return result
