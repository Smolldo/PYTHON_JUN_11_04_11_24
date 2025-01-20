a = 'Hello'

b = "комп'ютер"

#конкатенація
d = a + ' ' + b
# print(d)

c = 'Він сказав: \n"sdfsdfs"'

'''

sdfsdf
sdfsdf
sdfsdfs
sdfsdfs
sfsdfsf
rdfgdfggdfgdf
'''

#Реплікація
g = 'cat '
# print(g * 5)


name = 'John'
age = 25

result = 'Hello {}. I am {}'.format(name, age)

# print(result)

# print(f'Hello {name}. I am {age}')


txt = 'loreM ipSUM'
# .upper() - вс капсом(великі букви)

print(txt.upper())

# .lower() - все малими буквами
print(txt.lower())

# .title() - кожна перша буква кожного слова велика
print(txt.title())

# .capitalize() - перша буква першого слова велика
print(txt.capitalize())


# .find() - знаходить підрядок в рядку

t = 'Hello world'
print(t.find('aba'))

# .join() - об'єднання списку в рядок

l = ['aba', 'ba', 'gala', 'maga']

tt = ', '.join(l)

# print(tt)


# .replace() - заміняє частину рядка на щось інше

t = 'Hello world'
e = t.replace('l', '*', 1)
# print(e)


# .split() - перетворює рядок на список за розділювачем

t = 'Hello, world, lorem ipsum'
p = t.split(', ', 1)
# print(p)


# .strip() - прибирає пробіли на початку і кінці рядка

s = ' John '
# print(s.strip())




# списки - змінювані, впорядковані послідовності різних типів даних

l = list()
# print(l)

l1 = [1,2,3,4, 'asd', 'ada', p, True, [1,2,3]]

l2 = ['moloko', 'kovbasa', 'chipsi', 'cola']

print(l2[0])

#slice  [start : end : step]

print(l2[1:3])
print(l2[:3])
print(l2[1:])
print(l2[:])
print(l2[::-1])
print(l2[::2])