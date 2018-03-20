class Student:
    name = ''
    age = 0

    def __init__(self, name, age):
        print('__init__')
        self.name = name
        self.age = age

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


class StudentHomework:
    homework_name = ''

    def __init__(self):
        print('__init__')


student = Student('tingkl', 19)

student.print_file()

student1 = Student('yad', 2)
student2 = Student('mimi', 3)
student3 = Student('toby', 4)

print(id(student1))
print(id(student2))
print(id(student3))
