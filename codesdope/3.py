"""
Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
"""


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        return print(self.name, self.roll)

    def set_age(self, age):
        self.age = age

    def set_mark(self, mark):
        self.mark = mark

    def display_2(self):
        return print(self.name, self.age, self.mark, self.roll)


x = Student("oscar", "1901")
x.display()
x.set_age(22)
x.set_mark("A")
x.display_2()


print(x.name, x.roll, x.mark, x.age)
