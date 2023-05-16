'''
Hellow WOrld
https://indico.cern.ch/event/884989/contributions/3732167/attachments/1991200/3331806/Advanced_Programming_with_Python.pdf
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


def add_item(item, items=[]):
    items.append(item)
    return items
    
if __name__ == '__main__':
    v = add_item(1)
    print(add_item(2))
    print(add_item(3))
    
my_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

filtered_list = filter(lambda x: x > 0, my_list)

print(filtered_list)

for el in filtered_list:
    print(el)
    
print(list(filtered_list))
print(list(filter(lambda x: x > 0, my_list)))
print(list(map(lambda x: abs(x), my_list)))

lst1 = [0,1,2,3,4]
lst2 = [5,6,7,8]
print(list(map(lambda x, y: x + y, lst1, lst2)))

print(sum([0,1,2,3,4,5,6,7,8,9,10]))

from functools import reduce
print(reduce(lambda x, y: x + y, [0,1,2,3,4,5,6,7,8,9,10]))

i = 0
for el in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]:
    print(i, el)
    i += 1

for index, el in enumerate([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]):
    print(index, el)
        
letters = ['a', 'b', 'c', 'd']
numbers = [1,2,3,4,5]
for l,n in zip(letters, numbers):
    print(l,n)

print(list(zip(letters, numbers)))
print(dict(zip(letters, numbers)))

#help(zip)

x = [1,2,3,4]
y = x
y[0] = 'a'
print(x, y)

x = [1,2,3,4]
y = x.copy()
y[0] = 'a'
print(x, y)

x = [[1, 'a'] ,2,3,4]
y = x[:]
y[0] = 'a'
print(x, y)

x = [[1, 'a'] ,2,3,4]
y = x.copy()
y[0][0] = 'b'
print(x,y)

from copy import deepcopy
x = [[1, 'a'], 2,3,4]
y= deepcopy(x)
y[0][0] = 'b'
print(x, y)

x = [1, 10 ,2 , 9,3,8,4,6,5]
x = x.sort()
print(x)


x = [1, 10, 2, 9, 3, 8, 4, 6, 5]
x.sort()
print(x)

x = [1, 10, 2, 9, 3, 8, 4, 6, 5]
x = sorted(x)
print(x)

x = [1, 10, 2, 9, 3, 8, 4, 6, 5] 
print(x is sorted(x))

x = [1, 10, 2, 9, 3, 8, 4, 6, 5]
x.sort(reverse = True)
print(x)

employees = [(111, 'John'), (123, 'Emily'), (232, 'David'), (100, 'Mark'), (1, 'Andrew')] 
employees.sort(key=lambda x: x[0])
print(employees)

employees.sort(key = lambda x  : x[1])
print(employees)


employees.sort(key = lambda x  : x[1], reverse = True)
print(employees)

my_list = 5*['a']
print(my_list)

print(3 in [1,2,3,4,5])

x = ['a']
y = ['a']
print (x == y)

x = ('a')
y = ('a')
print(x is y)

my_tuple = (1,2,3)
print(my_tuple)

print(my_tuple[0])
#my_tuple[0]=0 

print(tuple([1,2,3]))

print({1,2,3,4})
print({1,2,3,4,4,4,4})

my_list = [1,2,3,4,4,4,4]
set(my_list)

A = {1,2,3}
B = {3,4,5}

print(f'A+B={A.union(B)}')
print(f'A-B={A-B}')
print(f'A*B={A.intersection(B)}')
print(f'A*0={A.intersection({})}')
print(f'A|B={A|B}')

pm = {'system', 'source', 'I_MEAS', 'I_REF'} 
signals = pm - {'system', 'source'} 
print(signals)

#help(set)

#signals[0]

print(next(iter(signals)))
list(signals)[0]

first, second = [1,2]
print(first, second)

first_S, second_S = {1,2}
print(first_S, second_S)


employees = [(111, 'John'), (123, 'Emily'), (232, 'David'), (100, 'Mark'), (1, 'Andrew')] 

for employee_id, employee_name in employees:
    print(employee_id, employee_name)


empty_set = {}
print (type(empty_set))

empty_set = set()
print (type(empty_set))

empty_set = ()
print (type(empty_set))


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict)

print(my_dict['a'])

for key in my_dict:
    print(key, my_dict[key])
    
for key, value in my_dict.items():
    print(key, value)
