from .person import Person
from .employee import Employee


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."
