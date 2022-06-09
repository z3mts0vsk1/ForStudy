# empty_list = []
# empty_list = list()
# print(type(empty_list))
#
# text = 'world'
#
# filled_list = [121313123, 123123.23123, 'strong', text, True, None, [1,2,3,4,5], 'Hello']
#
courses = {'History', 'Programming', 'Art', 'Literature', 'Physics', 'Math'}
# number = [1, 5, 6, 8, 4, 2]
# teste = ['History', 'Programming', 'Math', 'Literature', 'Physics', 'Math']
# courses2 = {'Art', 'Physics', 'Design', 'History'}
#
# # x = 5
# student = {'name': 'John', 'surename': 'Smith', 'age': 35}
# # number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(student.keys())
# print(student.items())
# print(student.values())
#
# for key in student.values():
#     print(key)

# for x in student:
#     print(student[x])


# odds = []
# evens = []
#
# for num in range(100):
#      if num % 2 == 0:
#          evens.append(num)
#      else:
#          odds.append(num)
#
# print(odds)
# #
# # for num in odds:
# #     print(num)
# #
# # for num in evens:
# #     print(num)
# #
# for num in range(100):
#     if num % 2 == 0:
#         print(num, 'Even')
#     else:
#         print(num, 'Odd')

# sample = (['one', 1], ['two', 2], ['three', 3])
# for x, y in sample:
#     print(x)
#     print(y)
#
# sample2 = ['one', 'two', 'three']
# for ind, val in enumerate(sample2, start=10 ):
#     print(f'{val}---{ind}')

# for num1 in range(10):
#     for num2 in range(10):
#         for num3 in range(10):
#             for num4 in range(10):
#                 print(num1, num2, num3, num4)

# for num in student:
#     print(num)
'''
for (variable) in (iterable)
    body of for
'''
# print(student['name'])
# print(student)


# x = student.pop('name') # это метод удаляет ключ, но можно сохраниить значение удаленного ключа
# print(x)
# del student['age']# удаление из словаря
# student2 = {'name': 'Mary', 'age': 25, 'phone': '555-555-55'}
# student.update(student2) # обновление одного словаря новым словарем
# student['phone'] = '555-555-55' # добавление в словарь новых ключей и значений
#print(len(student))


# print(student.get('phone', 'Doesn\'t exist'))

# test_dict = {'name': 'Hohn', 123: 'Hello', 0.23: 'One more', x: 'Five', True: 'True'}
# print(test_dict)


# empy_dict = {}
# empy_dict = dict()
# print(empy_dict)

# print(courses.intersection(courses2)) #поиск пересечений между чем либо
# print(courses2.difference(courses)) #поиск разницы между сетами
# print(courses.union(courses2)) # складывает два сета
#
# print(courses.issubset(courses2)) #под множество
# print(courses.issuperset(courses2))# над множество

# courses.update(number) # добавить сет нубмер в сет курсы
# print(courses)

#courses.clear() очистить

# courses.add('English')
# courses.pop()
# print(courses)

# courses.pop()
# print(courses)

# courses.remove('Math')
# print(courses)

#empty_set = set()

#print(type(courses))

# courses = list(courses)
# courses[3] = 'one'
# courses = tuple(courses)
# print(courses) # способ добавление чего либо в кортеж. меняем в список, добавляем, меняем в кортеж и выводим
# у кортежа всего два метода index и count

#print(tuple(courses))

# list1 = [1]
# print(type(list1))
#
# tuple1 = (1,)
# print(type(tuple1))

# empty_tuple = tuple()
# print(type(empty_tuple))


# tester2 = teste.copy()
#
# teste[0] = '1History'
# tester2[3] = 'Programming'
#
# print(teste)
# print(tester2)
#
# print(courses + number)

# courses_str = './ '.join(courses) #соединяет элементы списка в строку используя делитеь
# print(courses_str)

# a, b, c = input('Enter tringle sides.').split()
# print(a, b, c)

# new_list = 'Hello world'.split() # разделить строку на элементы, если в скобках пропуст то делитель будет пробел
# print(new_list)
# new_list.reverse()
# print(new_list)

#print(list('Hello world'))

#print('Math' in courses)#выводит булиан труе или фалсе при проверке

#print(courses.count('Math'))# считает кол-во искомого

# print(courses.index('Math', 3))
# print(courses[courses.index('Math')])


# print(min(courses))
# print(max(courses))
# print(sum(number))
#
# print(list('number'))



# print(sorted(courses))


# print(courses)
# print(reversed(courses))
# print(list(reversed(courses)))
# print(courses)

# print(courses)
# courses.reverse() #развернуть список
# print(courses)


# print(courses)
# courses.sort() #sort сортировка по альфавиту
# print(courses)
#
# print(number)
# number.sort(reverse=True) #sort сортировка по альфавиту (UTF), reverse=True - сортировка в обратную сторону
# print(number)


# courses.append('Art') #добавляет в конец списка
# print(courses)
# courses.insert(1, 'English') #добавляет с список по индексу
# print(courses)
#
# courses2 = ['Economics', 'Marketing']
# courses.append(courses2)
# print(courses)
#
# courses.extend(courses2) # extend способ расширить список, требует обьект который можно разложить на части
# print(courses)
#
# courses3 = 'Economics'
# courses.extend(courses3)
# print(courses)

# courses.remove('Math')
# print(courses)
#
# deleted = courses.pop(0) #метод поп моэно назначить переменной
# print(courses)
# print(deleted)




# test_list = [1, 2, 3]
# print(test_list)
#
# test_list[1] = 777
# print(test_list)