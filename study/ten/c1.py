# coding=utf-8
import re
a = 'C0C++7Java8C#9Python6Javascript'
print(a.index('Python') > -1)
print('Python' in a)

r = re.findall('Python', a)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')


r = re.findall('\d', a)
print(r)

r = re.findall('\D', a)
print(r)


s = 'abc, acc, adc, aec, afc, ahc'
r = re.findall('a[cf]c', s)
print r

r = re.findall('a[^cf]c', s)
print r

r = re.findall('a[c-f]c', s)
print r


a = '\tpython11 java\n345php\r'

r = re.findall('[0-9]', a)
print r

r = re.findall('[^0-9]', a)
print r

r = re.findall('\w', a)
print r

r = re.findall('\W', a)
print r

r = re.findall('[a-z]{3,6}', a)
print r

r = re.findall('[a-z]{3,6}?', a)
print r


a = 'pytho0python1pythonn2'
r = re.findall('python?', a);

print r

r = re.findall('python+', a);

print r

r = re.findall('python*', a);

print r


language = 'PythonC#\nJavaPHPC#'

r = re.findall('c#.', language, re.I)

print r

# re.S 使.可以匹配换行符
r = re.findall('c#.', language, re.I | re.S)

print r


language = 'PythonC#JavaPHPC#'


r = re.sub('C#', 'GO', language)
print r

r = re.sub('C#', 'GO', language, 1)
print r

print language.replace('C#', 'GO')


def convert(value):
    if __name__ == '__main__':
        print value.span(), value.group()
    matched = value.group()
    return '!!' + matched + '!!'


r = re.sub('C#', convert, language)
print r
