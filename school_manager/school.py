SCHOOL_NAME = "Tri Chandra School"

def ring_bell():
    print(". . Ringing!")

class Student:
    def __intit__(self, name, roll, grade):
        self.name = name
        self.roll = roll
        self.grade = grade

    def attend(self):
        print(f"{self.name} is present !!")


class ClassRoom:
    def __init__(self, teacher):
        self.teacher = teacher

