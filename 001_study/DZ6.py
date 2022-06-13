"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object
import datetime

# sample1 = 'Jan 1 2014 2:43PM'
# str_to_dt = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
# print(type(str_to_dt))
# print(str_to_dt)
#
# sample2 = '14:20 10/12/22'  # YY/MM/DD
# str_to_dt2 = datetime.datetime.strptime(sample2, '%H:%M %d/%m/%y')
# print(type(str_to_dt2))
# print(str_to_dt2)
#
# sample3 = 'Tuesday, September 24, 2019'
# str_to_dt3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
# print(type(str_to_dt3))
# print(str_to_dt3)
#
# sample4 = '01.01.1970 - 00:00:01'
# str_to_dt4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
# print(type(str_to_dt4))
# print(str_to_dt4)




# Write a program to print yesterdays, today and tomorrow dates
# today = datetime.date.today()
# tdelta = datetime.timedelta(1)
# print(f'Yesterday was: {today - tdelta}')
# print(f'Today is: {today}')
# print(f'Tommorrow will be: {today + tdelta}')



# Write a program to convert given timestamp to dd.mm.yyyy format
# some_day = 1014163200
# dt = datetime.datetime.fromtimestamp(some_day)
# print(type(datetime.datetime.fromtimestamp(some_day)))
# print(dt)
# print(dt.strftime('%d.%m.%Y'))




# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)
def timestamp():
    tdelta2 = datetime.timedelta(weeks=2)
    timestamp1 = float(input(f'Please input timestamp: '))
    ts1_dt = datetime.datetime.fromtimestamp(timestamp1)
    dt2 = ts1_dt - tdelta2
    timestamp2 = datetime.datetime.timestamp(dt2)
    print(ts1_dt)
    print(f'New timestamp is:{timestamp2}')
    print(datetime.datetime.fromtimestamp(timestamp2))

timestamp()


