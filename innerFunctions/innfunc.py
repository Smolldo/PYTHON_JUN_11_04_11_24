# map - застосовує до кожного елемента послідовності/колекцію якусь дію(функцію)

def squared(x):
    return x ** 2

l1 = [1,2,3,4,5]

nums_in_square = list(map(squared, l1))

print(nums_in_square)


# filter - фільтрує

def is_even(x):
    return x % 2 == 0

# even = list(filter(is_even, l1))

even = list(filter(lambda x: x % 2 == 0, l1))

# print(even)


from functools import reduce

def add(x, y):
    return x + y

l2 = [1,2,3,4,5,6,7,8,9,]

total = reduce(add, l2)
print(total)


# sorted - сортує

l3 = [3,6,3, -19, 6,8,9,1212121,6,4,3]
s = sorted(l3, reverse=True)
print(s)

# sum - знаходить суму усіх елементів послідовності
print(sum(l2))

#len - повертає довжину колекції/послідовності
print(len(l3))

# max - повертає максимальне значення з послідовності
print(max(l3))

#min - мінімальне значення
print(min(l3))


#any / all
values = [0, None, False, 1]
res = any(values)
print(res)

words = ['apple', 'banana', 'cherry']
res1 = all(words)
print(res1)


for i, word in enumerate(words):
    print(i + 1, word)



names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
comb = list(zip(names, ages))
print(comb)


# Напишіть програму, яка об'єднує два списки чисел, відфільтровує парні числа та обчислює їхні квадрати. 
# Використовуйте функції zip, filter, та map.

def dva_spiski(list1, list2):
    combined = zip(list1, list2)
    
    merged = [num for pair in combined for num in pair]

    even = filter(lambda x: x % 2 == 0, merged)

    squared = map(lambda x: x * x, even)

    return list(squared)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

res = dva_spiski(l1, l2)
print(res)



import math as m 

print(m.pi)

n = 5.53

print(m.ceil(n))
print(m.floor(n))

print(m.sqrt(16))

a = 4
b = 3
c = m.sqrt((a**2)+ (b**2))
print(c)