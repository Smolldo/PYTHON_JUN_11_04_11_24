def hello():
    print('hello world')


# hello()
first = 'Bob'

def name(name):
    print(f'Hello, {name}!')


name('John')
name('Jack')
name(first)


def add(x, y):
    return x + y

def next(x):
    return x * 3, x * 4

res = add(3,5)

print(next(res)) 



def mult(a, b = 5, c = 10):
    return f'a = {a}, b = {b}, c = {c}'

print(mult(12))
print(mult(b = 10, a = 5, c = 7))
print(mult(3, b = 22))



l1 = [1,2,3,4,5,6,7,8,9, -2]


# max_num = l1[0]

# for i in l1:
#     if i > max_num:
#         max_num = i

# print(min_num)


def min_num(x):
    mi_n = min(x)
    ma_x = max(x)

    return mi_n, ma_x

print(min_num(l1))


# global local 

x = 50

def ololo():
    global x
    x = 20
    return x


print(ololo())
print(x)


def lol(*args, **kwargs):
    return args, kwargs

print(lol(1,2,3,4,5,6,7,8,9, name = 'John', age = 23))



import module as m

from module import *

from module import add as ololo

print(ololo(3,5))