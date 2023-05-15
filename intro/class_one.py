'''
Hellow WOrld
'''
import this

print('Hello World')    


x = 3
y = x
(y, x)

x = -5

if x > 0:
    label = 'Pos'
else:
    label = 'Neg'
print(label)

'''
Create a python dicitionary of 5 countries and capitals:
'''


x = - 5
label = 'Pos' if x > 0 else 'Neg'
print(label)

my_string = 'My string'
result = my_string.replace('M','T')
print(result)
print(my_string)

for s in 'My string':
    print(s)

from datetime import date
print('Today is ' + str(date.today()) + '.')

print('Today is {} and number {}.'.format(date.today(), [1, 2, 3]))

print(f'Today is {date.today()}')

if 'sub' in 'substring':
    print('True')

print(dir(list))

print('my first sentence'.upper())

from enum import Enum
class QhBrowserAction(Enum):
    QUERY_BUTTON_CLICKED = 1
    SAVE_BUTTON_CLICKED = 2
    DATA_CHANGED = 3
    QH_NAME_CHANGED = 4
    SLIDER_MOVED = 5
    
a = QhBrowserAction.DATA_CHANGED
print(a.name, a.value)

a_next = QhBrowserAction(a.value + 1)
print(a_next)

if a_next == QhBrowserAction.QUERY_BUTTON_CLICKED:
    print('True')

if a_next == QhBrowserAction.QH_NAME_CHANGED:
    print('IN state {} '.format(a_next.value))
    
my_list = [1, 'b', True]

print(my_list)

print(my_list[0])
my_list[1] = 0
print(my_list)
my_list.append(1)
print(my_list)

my_list = my_list + [1, 'b']
print(my_list)

my_list += [3]
print(my_list)

my_list += [3]
print(my_list)

my_list.append([1, 'a'])
print(my_list)

my_list.extend([5, 1])
print(my_list)

my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)

print(0 > 1e-16)

my_list = [1/(i+1) for i in range(10)]
print(my_list)

my_list = [i for i in range(10) if i >  4]
print(my_list)


x = [x**2 for x in range(10)]
print(x)

import datetime
print(str(datetime.datetime.now()))


# print(datetime.datetime.now())
# for x in ((x+1)**2 for x in range(int(1e7))):
#     x**(-1/2)
# print(datetime.datetime.now())

# lst = [(x+1)**2 for x in range(int(1e7))]
# for x in lst:
#     x**(-1/2)
# print(datetime.datetime.now())

x = iter(range(10))
print(next(x))
print(next(x))

x = (x**2 for x in range(10))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(x)
print(list(x))
