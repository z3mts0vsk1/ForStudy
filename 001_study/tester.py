# string comment

'''
multi row comment
comment 1
comment 2
comment 3
'''

x = 5 # peremennqe po pravilu pishutsja s bukv ili _
print(x)

number_int = 45 # integer celqe 4isla
number_float = 45.2 # drobnqe 4isla

print(type(number_int))

text_str1 = 'Hello world'
text_str2 = "Hello world"
text_str3 = '''Hello world''' # тройные ковычки запоминают перенос строк
text_str4 = """Hello world"""

print(type(text_str1))

bool_type = False
bool_type2 = True

print(type(bool_type))

noon_type = None

'''
простые типы данных выше урок
'''

print(5 ** 2)

# возведение в степень 0.5 это вычисление квадратного корня. все идет их математики

a = 'I was born'
b = 1994

# конкатенация прибавление одной строки к другой

print(str(b) + ' ' + a)

# строки можно складывать и умножать но не больше

print(type(str(b))) # str(b) конвертация в другой тип данных

print(a, b)

b = '125.125'
print(int(float(b))) #int(b) or float(b) конвертация цисел или строк в целые и дробные числа

a = 5
a += 2
print(a)

# method HELP выводит инфо об классах или прочем

#user_input = input(' ')
#print(user_input)

a, b, c = float(input('Side A:')), float(input('Side B:')), float(input('Side C:'))
perimeter = (a + b + c) / 2

triangle_area = (perimeter * (perimeter - a) * (perimeter -b) * (perimeter - c)) ** 0.5

print(triangle_area)