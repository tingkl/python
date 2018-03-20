# coding=utf-8

import sys

# reload(sys)
# sys.setdefaultencoding('utf8')


def add(x, y):
    rs = x + y
    print(rs)
    return rs


add(1, 2)


def damage(skill1, skill2):
    _damage1 = skill1 * 3
    _damage2 = skill2 * 2 + 10
    return _damage1, _damage2


damages = damage(1, 2)
print type(damages)
print damages[0], damages[1]

# 序列解包
damage1, damage2 = damage(1, 2)
print damage1, damage2

# 元组简写
d = 1, 2, 3

a, b, c = d

print d, type(d)
print a, b, c

print sys.getdefaultencoding()


def student(name='name', gender='male'):
    print name, gender


student('鸡小萌')
student('鸡小萌', '女')

print '你好'


var = 30


def changeVar(newvar):
    global var
    var = newvar
    print(var)


changeVar(4)
print(var)

