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

    # USER MENU
while True:
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

        # REGION OF BIRTH PART
    elif user_choice == '3':

        region = user_id[7:10]

        if int(user_id[7:10]) in range(1, 11):
            bregion = 'in Kuressaare haigla'
        elif int(user_id[7:10]) in range(11, 20):
            bregion = 'in Tartu Ülikooli Naistekliinik'
        elif int(user_id[7:10]) in range(21, 151):
            bregion = 'in Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
        elif int(user_id[7:10]) in range(151, 161):
            bregion = 'in Keila haigla'
        elif int(user_id[7:10]) in range(161, 221):
            bregion = 'in Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
        elif int(user_id[7:10]) in range(221, 271):
            bregion = 'in Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
        elif int(user_id[7:10]) in range(271, 371):
            bregion = 'in Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
        elif int(user_id[7:10]) in range(371, 421):
            bregion = 'in Narva haigla'
        elif int(user_id[7:10]) in range(421, 471):
            bregion = 'in Pärnu haigla'
        elif int(user_id[7:10]) in range(471, 491):
            bregion = 'in Haapsalu haigla'
        elif int(user_id[7:10]) in range(491, 521):
            bregion = 'in Järvamaa haigla (Paide)'
        elif int(user_id[7:10]) in range(521, 571):
            bregion = 'in Rakvere haigla, Tapa haigla'
        elif int(user_id[7:10]) in range(571, 601):
            bregion = 'in Valga haigla '
        elif int(user_id[7:10]) in range(601, 651):
            bregion = 'in Viljandi haigla'
        elif int(user_id[7:10]) in range(651, 701):
            bregion = 'in Lõuna-Eesti haigla (Võru), Põlva haigla'
        elif int(user_id[7:10]) in range(701, 1000):
            bregion = 'out if Estonia'
        else:
            bregion = "Unknown"

        # PRINT MESSAGE
        if bregion == "Unknown":
            print(f'Can\'t determine region of birth.')
        else:
            print(f'You was born {bregion}')

        # ID VALIDATING PART "Moodul 11"
    elif user_choice == '4':

        key_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        key_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        x_1 = int(user_id[0]) * 1 + int(user_id[1]) * 2 + int(user_id[2]) * 3 + int(user_id[3]) * 4 + int(user_id[4]) * 5 + int(user_id[5]) * 6 + int(user_id[6]) * 7 + int(user_id[7]) * 8 + int(user_id[8]) * 9 + int(user_id[9]) * 1
        x_2 = x_1 // 11
        print(x_1)
        print(x_2)

        y_1 = int(user_id[0]) * 3 + int(user_id[1]) * 4 + int(user_id[2]) * 5 + int(user_id[3]) * 6 + int(user_id[4]) * 7 + int(user_id[5]) * 8 + int(user_id[6]) * 9 + int(user_id[7]) * 1 + int(user_id[8]) * 2 + int(user_id[9]) * 3
        y_2 = y_1 // 11
        print(y_1)
        print(y_2)

        if x_1 - (x_2 * 11) == int(user_id[10]):
            id_status = 'valid by first run'
        elif x_1 - (x_2 * 11) >= 10 and y_1 - y_2 * 11 < 10 and y_1 - y_2 * 11 == int(user_id[10]):
            id_status = 'valid by second run'
        elif y_1 - y_2 * 11 >= 10 and int(user_id[10]) == 0:
            id_status = 'valid by third run'
        else:
            id_status = 'Not valid'

        if id_status == 'Not Valid':
            print(f'Your ID number is not valid.')
        else:
            print(f'Your ID number is {id_status}.')

    elif user_choice == '0':
        print('Good bye. ')
        break
    else:
        print('Choice out of range.')