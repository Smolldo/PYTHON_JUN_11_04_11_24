# < <= > >= == !=

# if 7 < 3:
#     print(True)
# elif 7 == 7:
#     print(True)
# else:
#     print(False)

grade = 70


# if grade >= 90:
#     print('ocinka A')
# elif grade >= 80:
#     print('ocinka B')
# elif grade >= 70:
#     print('ocinka C')
# else:
#     print('ne zdav')


# and or not

#оператори - значки(дії)
# операнди - те над чим виконується дія

# age = 25

# if age >= 18 and age <=60:
#     print('vi dorosli')


# day = 'monday'

# if day == 'saturday' or day == 'sunday':
#     print('weekend')


# weekend = False

# if not weekend:
#     print('robochii den')





#loops
# for i in range(1, 11, 3):
#     print(i)

lst1 = [1,2,3,4,5,6,7,8,9]

# for i in lst1:
#     print(i * 2)
# else:
#     print('done')

lst1 = [1,2,3,4,5,6,7,8,9]

lst2 = []

# for i in lst1:
#     if i % 2 == 0 and i > 5 and i < 8:
#         lst2.append(i)
# print(lst2)



#while
a = 0

# while a < 20:
#     print(')')
#     a += 1

lst1 = [1,2,3,4,5,6,7,8,9]
target = 6

for i in lst1:
    if i == target:
        print(f'{i} znaydeno')
        break
else:
    print('ne znaydeno')


for i in lst1:
    if i % 2 != 0:
        continue
    else:
        lst2.append(i)
print(lst2)

# тернарні вирази

num = -7

ispositive = 'positivne' if num > 0 else 'negativne'
print(ispositive)

import random

comp = random.randint(1,10)

while True:
    inp = int(input('Enter chislo'))

    if inp == comp:
        print('correct')
        break
    else:
        print('lsdfsdf')