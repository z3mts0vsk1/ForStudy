#N N1 #################
# name = input(f'Please write your name:')
# lastname = input(f'Please write your lastname: ')
# age = input(f'Please write your age: ')
#
# print(f'Hello, {lastname} {name}. Your age is: {age}')

# N2 ##################
# c2=a2+b2
# c = sqrt(a+a + b+b)
#
# a = input(f'Write lenght of catet a:')
# b = input(f'Write lenght of catet b:')
#
# c = ((int(a) * int(a)) + (int(b) * int(b))) ** 0.5
#
# print(c)


### N3 ######################
# a, b, c = float(input('Side A:')), float(input('Side B:')), float(input('Side C:'))
#
# if c ** 2 == a ** 2 + b ** 2:
#     print('Triangle is straight!')
# else:
#     print(f'Triangle is not straight!')

### N4 ################################
# sample_list = [3, 2, 1, 6]
# sample_list2 = ['Daniil', 'Danik', 'Denis']
#
# print(sample_list)
# print(sample_list2)
# sample_list.reverse()
# sample_list2.reverse()
# print(sample_list)
# print(sample_list2)


# new_list = input(f'Please write one sentence:').split() # разделить строку на элементы, если в скобках пропуст то делитель будет пробел
# print(new_list)
# new_list.reverse()
# print(new_list)

### N5 ##########################
# kortez = (1, 2, 3, 4, 5, 6)
# kortez2= ('Kot', 'Dog', 'Bog')
# kortez = list(kortez)
# kortez[2] = kortez2
#
# print(kortez)


# N6
lis = [1, 2, 3, 4, 7, 9, 9]
lis = list(lis)
num = ()
print(lis.count(9))

if lis.count(1) >=2:
    lis = '1'
elif lis.count(2) >= 2:
    lis = '2'
elif lis.count(3) >= 2:
    lis = '3'
elif lis.count(4) >= 2:
    lis = '4'
elif lis.count(7) >= 2:
    lis = '5'
elif lis.count(9) >= 2:
    lis = '9'

print(lis)


