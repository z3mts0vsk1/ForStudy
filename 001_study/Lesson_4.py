# ID CODE ENTRY
while True:
    try:
        user_id = input('Please enter your ID: ')
        if user_id.lower() == 'exit':
            quit()
        int(user_id)
        if len(user_id) != 11:
            raise UserWarning
    except ValueError:
        print('Code is not numeric.')
    except UserWarning:
        print('Code is not 11 digit long!')
    else:
        break

while True:
    # USER MENU
    user_choice = input('Please choose:\n'
                        '1.Gender\n'
                        '2.Date of birth\n'
                        '3.Region of birth\n'
                        '4.Validate\n'
                        '0.Exit\n'
                        '---> ')
    if user_choice == '1':
        # DETERMINE GENDER
        if int(user_id[0]) % 2 == 0:
            gender = 'Female'
        elif user_id[0] in ['0', '9']:
            gender = 'Unknown'
        else:
            gender = 'Male'
        # PRINT MESSAGE
        if gender != 'Unknown':
            print(f'You are {gender}.')
        else:
            print('Cant\'t determine gender.')

    elif user_choice == '2':
        # DD.MM.YYYY
        byear = user_id[1:3]
        bmonth = user_id[3:5]
        bday = user_id[5:7]

        if user_id[0] in ['1', '2']:
            bcent = '18'
        elif user_id[0] in ['3', '4']:
            bcent = '19'
        elif user_id[0] in ['5', '6']:
            bcent = '20'
        elif user_id[0] in ['7', '8']:
            bcent = '21'
        else:
            bcent = 'Unknown'

        # PRINT MESSAGE
        if bcent == 'Unknown':
            print(f'Can\'t determine date of birth.')
        else:
            print(f'Your date of birth is {bday}.{bmonth}.{byear}')
    elif user_choice == '3':
        pass
    elif user_choice == '4':
        pass
    elif user_choice == '0':
        print('Good bye. ')
        break
    else:
        print('Choice out of range.')

# while True:
#     try:
#         user_input = input('Please enter ID: ')
#         int(user_input)
#         if len(user_input) != 11:
#             raise UserWarning
#     except ValueError:
#         print('Code is not numeric')
#         continue
#     except UserWarning:
#         if len(user_input) < 11:
#             print('Too short')
#         else:
#             print('Too long')
#         continue
#     break
# print('User id:', user_input)


# else:
    #     print('User id:', user_input)
    # finally:
    #     print('All is good')

#except исключение

# if user_input.isdecimal():


# condition = True
# while condition:
#     user_input = input('Please choose:\n1.Print\n2.Exit\n--> ')
#     if user_input == '1':
#         print('All is good.')
#     elif user_input == '2':
#         print('Good bye')
#         condition = False
#     elif user_input == '3':
#         # ID entry cycle
#         while True:
#             user_id = input('Please enter ID: ')
#             if len(user_id) != 11:
#                 print('Wrong ID')
#                 continue
#             else:
#                 break
#         print(user_id)
#     else:
#         print('Wrong choice')
#     print('Hello world')

#pass проигнорируй
#break остнови цикл ближайший
# continue разорви круг цикла, и вернется в начало
# exit() and quite() останови программу. используется для граф интерфейса

# condition = True
# x = 0
# while condition:
#     if x >100:
#         condition = False
#     print(x)
#     x += 1

# distance_to_target = float(input('How many KM:')) * 1000
# current_position = 0
#
# step = 0.4 # meters
#
# step_cnt = 0
#
# while current_position <= distance_to_target:
#     current_position += step
#     step_cnt += 1
#     if step_cnt % 100 == 0:
#         print(step_cnt)


# x = 0
#
# while x < 100:
#     print('I can\'t stop')
#     print(x)
#     x += 1