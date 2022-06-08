
def print_100():
    print(100)

def return_100():
    return 100

#print_100()

#print(return_100())


def print_x():
    x = 10
    print(x)


x = 100
print_x()

def double(number):
    return number * 2

print(double(10))

'''
'''
def triple(number):
    return number * 3

print(triple(10))
print(triple(double(10)))
'''

'''
def print_greeting(name, surname):
    print(f'Hello {name.capitalize()} {surname.capitalize()}')

name = input('Enter name: ')
surname = input('Enter surname: ')#'zemts'
print_greeting(name, surname)

print(area(10, 2))
'''
'''
def area(a, b):
    return f' Area is equal to {a * b}cm2'


def perimeter(a, b):
    return f' Perimeter is equal to{(a + b) * 2}cm'


def main():
    side_a, side_b = input('Please enter side A and side B:').split(",")
    print(area(int(side_a), int(side_b)))
    print(perimeter(int(side_a), int(side_b)))


main()

def fizz_buzz(start, end):
    for num in range(start, end):
        if num % 5 == 0 and num % 3 == 0:
            print(num, 'FizzBuzz')
        elif num % 3 == 0:
            print(num, 'Fizz')
        elif num % 5 == 0:
            print(num, 'Buzz')

fizz_buzz(40, 400)


def more_than_100(number):
    if number > 100:
        return 'Number is bigger than 100'
    elif number < 100:
        return 'Number if less than 100'
    else:
        return 'Number is equal to 100'


print(more_than_100(100))


employees = [('John', 'Smith', 35, 2500, 'male'),('Dan', 'Zemts', 25, 2000, 'male'),
             ('Lili', 'Silver', 15, 3500, 'female'),('Mary', 'Gold', 45, 3000, 'female'),]

def print_message(name, surname, age, salary, gender):
    if gender == 'male':
        result = f'His name is {name} {surname}. He is {age} years old. His salary is {salary:.2f} eur.'
        return print(result)
    elif gender == 'female':
        result = f'Her name is {name} {surname}. She is {age} years old. Her salary is {salary:.2f} eur.'
        return print(result)


for person in employees:
    print_message(person[0], person[1], person[2], person[3], person[4])


#def some_function(a, b, c=10):
#    return a * b * c


#print(some_function(5, 4, 5))

def some_function(a, b, *args, **kargs):
    print(args)
    if args:
        for arg in args:
            print(arg, 'ARG')
    print(kargs)
    if kargs:
        for karg in kargs:
            print(karg, 'KARG')
    print(a + b)


some_function(2, 3, 5, 6, 7, 8)

some_function(2, 3, x=5, y=10, i=15)

import math

print(square_functions.square(4))

from math import *

print(double(2))
'''
