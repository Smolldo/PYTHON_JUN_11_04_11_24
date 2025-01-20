# Створіть три змінні, які будуть відповідати вашому прізвищу, ім’я та вашому класу навчання

first_name = 'Misha'

lastName = 'Honyk'

grade = 12


# Створіть змінну, що міститиме ваше ім'я, та змінну, що міститиме ваше прізвище.
#  Потім об'єднайте їх у змінну повного імені та виведіть у верхньому регістрі.


#конкатенація - склеювання рядків
fullName = first_name + ' ' + lastName

# print(fullName.upper())



# upper() - все велике. lower() - все маленьке. swapcase() - велике стає малим, а мале великим. capitalize() - перша буква  першого слова велика 
# title() - перша літера кожного слова велика

a = 'lorem ipSUM'

# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.capitalize())
# print(a.title())



# Створіть змінні для трьох ваших улюблених книг. Потім об'єднайте ці змінні в один рядок, розділений комами, і виведіть на екран.

book1 = "Harry Potter"
book2 = "The Lord of the Rings"
book3 = "1984"

# print(book1, book2, book3)

# f - рядок
# print(f'"{book1}", "{book2}", "{book3}"')


# Створіть змінну для вашого віку та змінну для віку вашого друга. Потім створіть змінну, що містить різницю у віці між вами та вашим другом, та виведіть на екран.
my_age = 25
friend_age = 27

diff = abs(my_age - friend_age) #модуль числа. повертає додатнє число або 0. робить з від'ємного числа додатнє
# print(diff)



#numeric type int(), float(), complex 3j + 5
#boolean bool() 
#text str()

a = 32
# print(type(a))

a = str(32)
# print(a)
# print(type(a))

b = 3.12

# print(int(b))

c = [1]

# print(bool(c))


d = '23'
# print(int(23))


f = float(5)

# print(f)


p =  3.63

# print(round(p))


#    // - ділення націло

s = 10 // 6
# print(round(s))
# print(s)

# % - остача від ділення
s = 10 % 6
# print(s)

# ** - степінь числа

# print(2 ** 6) # 2 * 2 * 2 * 2 * 2 * 2


# print(2 * 3)
# print(2 ** 3) #2 * 2 * 2

