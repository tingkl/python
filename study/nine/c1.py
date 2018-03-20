# coding=utf-8
class Student:
    sum = 0

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print '类方法'

    @staticmethod
    def add(x, y):
        print '静态方法'
        print Student.sum
        return x + y

    def __init__(self, name, age):
        print('__init__')
        self.name = name
        self.age = age
        # Student.sum += 1
        # self.__class__.sum += 1
        self.__class__.plus_sum()
        print('当前班级学生总数为:' + str(self.__class__.sum))

    def __private_method(self):
        print('__表示私有方法，外部不能调用')

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


class StudentHomework:

    def __init__(self, homework_name):
        print('__init__')
        self.homework_name = homework_name
        self.__privateVar = 'private var'

    def do_homework(self):
        print(self.homework_name)


student = Student('tingkl', 19)

student.print_file()

student1 = Student('yad', 2)
student2 = Student('mimi', 3)
student3 = Student('toby', 4)

print(id(student1))
print(id(student2))
print(id(student3))

print student1.__dict__
print Student.__dict__

print student1.add(1, 2)
print Student.add(2, 3)

# print student1.__private_method


print '--------------'
homework1 = StudentHomework('yw')
homework1.homework_name = 'sx'

homework1.__privateVar = '这是新创建了一个属性，私有变量被python改名了_StudentHomework__privateVar'

print homework1.__dict__
print homework1._StudentHomework__privateVar
