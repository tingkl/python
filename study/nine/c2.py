# coding=utf-8
from c6 import Human


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def do_homework(self):
        super(Student, self).do_homework() 
        print('english homework')


student1 = Student('high school', 'tom', 18)
print Student.sum
print student1.__dict__

student1.do_homework()
student1.get_name()

