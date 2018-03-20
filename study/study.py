# coding=utf-8
# print('hello python')

# 流程控制语句
'''
条件控制 循环控制 分支

if else for while switch

'''

a = 1
b = 2
mode = a > b
if mode:
    print('go to left')
else:
    print('go to right')


if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')

counter = 10

while counter:
    print('i am while', counter)
    counter -= 1
else:
    print('EOF')

print('列表')
# 主要是用来遍历/循环 序列或者集合 字典
a = ['apple', 'orange', 'banana', 'grape']
for item in a:
    print item
else:
    print('fruit is gone')

print('元组')
a = ('apple', 'orange', 'banana', 'grape')
for item in a:
    print item
else:
    print('fruit is gone')

print('集合')
a = {'apple', 'orange', 'banana', 'grape'}
for item in a:
    print item
else:
    print('fruit is gone')

print('字典')
a = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'grape'}
for item in a:
    print a[item]

print('break & continue')
a = ['apple', 'orange', 'banana', 'grape']
for item in a:
    if item == 'apple':
        continue
    if item == 'grape':
        break
    print item
else:
    print('break不会执行else')


# for (i = 0; i < 10; i++) {
# }
print('正序')
for x in range(0, 10):
    print(x)
print('倒序')
a = [1, 2, 3, 4, 5, 6, 7, 8]
for x in range(len(a), 0, -1):
    print(x)

print(a[0::2])
