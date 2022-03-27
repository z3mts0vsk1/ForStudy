string_sample = "Hello world world"
              #  01234567890123456
              #             -3-2-1
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der Fluß"

# /n перенос строки
# [1:2:3] 1 start 2 end 3
# == сравнение
print(string_sample[4])
print(len(string_sample) - 1)

print(string_sample[4:6:1])

print("world" in string_sample)
print(type("world" in string_sample))

print(string_sample.upper()) #в верхний регистр
print(string_sample.isupper()) # проверка на
print(german_sample.lower()) #в нижний регистр
print(string_sample2.islower()) #
print(german_sample.casefold()) #конвертация сложных букв языков в простое

print(string_sample3.strip()) #strip вырезает пробелы слева и справа
#lstrip() слева
#rstrip() справа
print(string_sample2.capitalize())#capitalize первую букву заглавной остальные в прописные
print(string_sample2.swapcase())

print(string_sample.replace('Hello', 'Dildo')) # заменяет чтото на чтото

print(string_sample.find('world'))#находит

print(string_sample.count('world'))#считает

a = 'hello'
b = 'world'


emp_name = 'John'
emp_age = 30
emp_salary = 1000

emp_message = f'Hi, my name is {emp_name}. I am {emp_age} years old. My salary is {emp_salary:.2f}.'
print(emp_message)

byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_sting)
print(byte_sting.decode('utf-16'))

isikukood = '39412021526'

if len(isikukood) !=11:
    print('Wrong code!')

else:
    print('ID: ' + isikukood)

if len(isikukood) == 11:
        print('Wrong code!')
else:
        print('ID: ' + isikukood)

user_choice = input('1.Hello\n2.World\n3.Good bye\n---> ')

if user_choice == '1':
    print('Hello')
elif user_choice == '2':
    print('World')
elif user_choice == '3':
    print('Good bye')
else:
    print('Choice out of range')