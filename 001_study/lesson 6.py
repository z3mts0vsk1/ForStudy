# import calendar
#
# # print(calendar.month(2022, 6))
# # print(calendar.calendar(2022))
#
#
# #print(calendar.HTMLCalendar().formatyear(2022))
#
# print(calendar.weekday(2022, 6, 10)) # вывод дня недели
#
# print(calendar.isleap(2024)) # проверка на весокосность года
# print(calendar.isleap(2022))
#
# print(calendar.leapdays(2000, 2021)) # посчитать количество весокосныз лет в диапозоне

import time

# time.sleep(5) # обязательная пауза в секундах
# print(time.time())

# start = time.time_ns() # ns vмикро секунды
# time.sleep(5)
# stop = time.time()
#
# print(stop - start)

#print(time.asctime()) # выводит строку с датой временем

# print(time.gmtime()) # время по гринвичу в кортеже
# print(time.localtime()[0]) # местное время в кортеже
#

import datetime

# d = datetime.date(2018, 7, 22)
# print(d)
# print(type(d))
#
today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
#
# print(type(today - d))
#
# #date1 - date2 = timedelta
# #date1 - timedelta = date2
#
tdelta = datetime.timedelta(1)
print(tdelta)
print(today - tdelta)
#
# bday = datetime.date(2022, 12, 2)
# till_bd = bday - today
# print(bday - today)
# print(till_bd)
#
# print(today.weekday())
# print(today.isoweekday())


# t = datetime.time(12, 24, 30)
# print(type(t))
#
# dt = datetime.datetime(2022, 7, 14, 18, 20, 15, 100000)
# # print(dt)
# # print(dt.time())
# # print(dt.date())
# #
# # dt_delta = datetime.timedelta(days=5, hours=5, minutes=5)
# # print(dt - dt_delta)
#
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# print(dt_today)
# print(dt_now)
#
# print(dt.timestamp())
# print(datetime.datetime.fromtimestamp(12321312321))

# today = datetime.datetime.today()
#
# print(today.strftime('%A')) # вывести строку из формата datetime
# print(today.strftime('%X'))
# dt_str = 'November 30, 2022 17:30'
# str_to_date = datetime.datetime.strptime(dt_str, '%B %d, %Y %H:%M') # перевод строки в формат datetime
# print(type(str_to_date))