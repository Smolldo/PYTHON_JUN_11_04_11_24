#кортеж - tuple 

t1 = (1,2,3,4)

t2 = ('a', 'a', 'a', 'a', 'b', 2, 3, True)

t = t2.count('a') #рахує кількість входження елем. в кортеж
# print(t)

t3 = t2.index('a')
# print(t3)


# множина - set - колекція унікальних елементів

s = set()
s1 = {1,2,3}

l1 = [1,1,1,1,2,2,2,3,3,3,3,]
print(set(l1))

f = 'Hello world'
print(set(f))


# add() - додає елемент до множини
s1.add(6)
# print(s1)


# s1.clear() - очищає множину

# s1.copy() - копіює множину

s2 = s1.copy()  # s1 = {1,2,3,6}  s2 = {1,2,3,6}

# print(s1 == s2)

#discard - прибирає елемент з множини. якщо елемента немає, помилка не виникне
s1 = {1,2,3,6}

# s1.discard(9)
# print(s1)

# pop() - повертає елем. і видаляє його.

# s1.pop()
# print(s1)


# remove() - видаляє елемет з множини

s3 = {'a', 'b', 'c'}

s3.remove('b')
# print(s3)


# Словники

# dict()

d1 = {
    'name': 'John',
    'age': 25,
    'haspet': False
}

# print(d1['name'])

# print(d1.get('city', 'nema takogo elementa'))

#додавання елементів
d1['city'] = 'Kyiv'
# print(d1)

# del
# del d1['age']
# print(d1)
d1 = {
    'name': 'John',
    'age': 25,
    'haspet': False
}

# print(d1.keys())
# print(d1.values())
# print(d1.items())


d2 = d1.pop('name')
# print(d2)
# print(d1)


# Створіть словник для збереження адрес друзів. Ключами будуть імена друзів, а значеннями — словники, 
# що містять вулицю, місто та поштовий код. Додайте адреси для трьох друзів та виведіть адресу одного з них.

friends = {
    'John': {
        'street': 'Nerter',
        'city': 'Night City',
        'index': '46001'
    },
    'Jack': {
        'street': 'Ololo',
        'city': 'novigrad',
        'index': '1398'
    },
}

print(f'{friends["John"]['city']}. i vylitsya {friends["John"]['street']}')