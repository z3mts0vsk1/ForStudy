# 0-100
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz

fizz = []
buzz = []
fizzbuzz = []

for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, 'FizzBuzz')
    elif num % 5 == 0:
        print(num, 'Buzz')
    elif num % 3 == 0:
        print(num, 'Fizz')


# for num in range(101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, 'FizzBuzz')
# print(fizz)
# print(buzz)
# print(fizzbuzz)



# fizz = []
# for num in range(100):
#     if num % 3 == 0:
#         fizz.append(num)
# for num in fizz:
#      print(num, 'Fizz')

# buzz = []
# for num in range(100):
#     if num % 5 == 0:
#         buzz.append(num)
# for num in buzz:
#      print(num, 'Bizz')
#
# fizzbuzz = []
# for num in range(100):
#     if num % 3 == 0:
#         fizzbuzz.append(num)
#     elif num % 5 == 0:
#         fizzbuzz.append(num)
# for num in fizzbuzz:
#     print(num, 'FizzBuzz')
#
# print(fizzbuzz)
# print(fizz, 'Fizz')
# print(buzz, 'Buzz')



# odds = []
# evens = []
#
# for num in range(100):
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)

# for num in odds:
#     print(num ** 2)
#
# for num in evens:
#     print(num ** 3)
#
# for num in range(100):
#     if num % 2 == 0:
#         print(num, 'Even')
#     else:
#         print(num, 'Odd')
