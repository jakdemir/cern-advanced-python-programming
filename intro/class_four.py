'''
Functions
'''

f = lambda x: x**2
print(f(2))

def f(x):
    return x**2

print(f(2))

def f(a, b, c=3):
    return a + b + c

print(f(1,2))

print(f(1,2,4))

lst = [1,2,3]
print(f(*lst))

dct = {'a':1, 'b' :2, 'c': 3}
print(f(**dct))

# query_params = {'db': "NXCALS", "signal": "I_MEAS", "t_start": "today", "t_end": "tomorrow"}
# call_db(**query_params)
# query_params['db'] = 'PM'
# call_db(**query_params)

def f(a, b, d, c=3):
    return a + b + c + d

def f(*args):
    print(len(args))
    return args[0]*args[1]*args[2]

print(f(1,10,'a'))

def f(**kwargs):
    return kwargs['a'] + kwargs['b']

print(f(a=1, b=2, c=3))

def f(arg, *args, **kwargs):
    return arg + sum(args) + kwargs['f']

print(f(1,2,3,4,5, f=6))

def f(a, b, *, c):
    return a+ b+ c

#print(f(1,2,3))

print(f(1,2, c=3))

def f(x):
    return x**2

def g(func, x):
    return func(x)

print(g(f, 2))

def f():    
    return 'a', 'b', 's' 

print(f())

first = list(f())

print(first)
#print(second)


first[1]= 2
print(first)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n - 1)
    
print(factorial(3))

#factorial(-1)

def factorial(n):
    if not isinstance(n, int) or n<=0:
        raise ValueError("Argument is not a positive integer")
    if n == 1:
        return 1
    else:
        return n*factorial(n - 1)

factorial(5)


def flatten_nested_lists(x):
    result = []
    for el in x:
        if isinstance(el, (list, tuple)):
            result.extend(flatten_nested_lists(el))
        else:
            result.append(el)
    return result


lst1 = [1]
lst2 = [1,2]
lst1.append(lst2)

print(lst1)

lst = [1,2,[3,4], [5,[6,7]]]

print(flatten_nested_lists(lst))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print([fib(i) for i in range(6)])

arguments = []
def fib(n):
    arguments.append(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print([fib(i) for i in range(6)])

print(arguments)

counts = {i: arguments.count(i) for i in range(max(arguments)+1)}
print(counts)


memo = {0:0, 1:1}
arguments = []
def fib(n):
    arguments.append(n)
    if(n not in memo):
        memo[n] = fib(n-2) + fib(n-1)
    return memo[n]

print([fib(i) for i in range(6)])

count = {i: arguments.count(i) for i in range(max(arguments)+1)}

print(count)

def argument_test_natural_number(f):
    def helper(x):
        if type(x) is int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial = argument_test_natural_number(factorial)
factorial(3)
#factorial(-1)


def argument_test_natural_number(f):
    def helper(x):
        if type(x) is int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper

@argument_test_natural_number 
def factorial(n):
    if n == 1:        
        return 1    
    else:        
        return n*factorial(n-1)
    
#factorial(-1)

def sum_aritmetic_series(n):
    return n * (n + 1)/2

sum_aritmetic_series(2)

@argument_test_natural_number
def sum_aritmetic_series(n):
    return n * (n + 1)/2

print(sum_aritmetic_series(2))

#print(sum_aritmetic_series(-1))

def memoize(f):
    memo = {}
    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return helper

arguments = []

@memoize
def fib(n):
    arguments.append(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print([fib(i) for i in range(6)])

count = {i: arguments.count(i) for i in range(max(arguments)+1)}
print(count)

import functools
@functools.lru_cache(maxsize=128, typed=False)
def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)

print(fib(6))

# Exercise 
# - write a decorator counting the number of times a function was called 
# - the same but for a varying number of parameters and keyword-argument

def call_counter(f):
    def helper(x, *args, **kargs):
        helper.count += 1
        return f(x, *args, **kargs)
    helper.count = 0
    return helper


@call_counter
def fun(x):
    return x

fun(1)
fun(2)
fun(3)

print(fun.count)


s = "Python"
itero = iter(s)
print(itero)

print(next(itero))
print(next(itero))
print(next(itero))
print(next(itero))
print(next(itero))
print(next(itero))
#print(next(itero))


def abc_generator():
    yield 'a'
    yield 'b'
    yield 'c'
    
x = abc_generator()

for i in x:
    print(i)

# next(x)
# next(x)


x = abc_generator()
print(next(x))
print(next(x))
# print(next(x))
# print(next(x))

def abc_generator():
    return "a"

x = abc_generator()

for i in x:   
    print(i)
    
print(type(abc_generator()))


def abc_generator():
    for char in ["a", "b", "c"]:
        yield char
        
for i in abc_generator():
    print(i)

print(type(abc_generator()))


def pi_series():
    sum = 0
    i = 1.0
    j = 1    
    while True:
        sum = sum + j/i 
        yield 4*sum
        i = i + 2
        j = j * -1
        
# for i in pi_series():
#     print(i)
    
def firstn(g,n):
    for i in range(n):
        yield next(g)


print(list(firstn(pi_series(), 8)))

import csv

with open('example.txt', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['date','# events'])

from contextlib import contextmanager

@contextmanager
def device():
    print("Check device")
    device_state=True
    print("Start device")
    yield device_state
    print("Stop device")

with device() as state:
    print("Stat is", state)
    print("Device is running")

device()

# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         break
#     except ValueError as err:
#         print("Error message:", err)
#         print("No valied number. Try again")

# try:
#     x = float(input("Your number: "))
#     inverse = 10/x
# except ValueError as err:
#     print("Error message: ", err)
#     print("No valid number. Try again")
# finally:
#     print("There may or may not have been an exception.")
# print("The inverse: ", inverse)

x = 5
y = 6

assert x < y, "x has to be smaller than y"



