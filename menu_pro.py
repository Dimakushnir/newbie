def showmenu():
    print ('\nM A I N   M E N U')
    print ('1. Print reversed string')
    print ('2. Print uppercased string')
    print ('3. Print lowercased string')
    print ('4. Print vertical string')
    print ('0. Exit')
    selected_option = int(raw_input('Select an option: '))
    return selected_option


def reversed_string(value):
    reversed_message = value[::-1]
    return reversed_message


def uppercase_string(value):
    return value.upper()


def lowercase_string(value):
    return value.lower()


def vertical_string(value):
    for character in value:
        print(character)


def mainmenu():
    loop_iterator = ''
    while loop_iterator == '':
        option = showmenu()
        if option == 1:
            entered_data = raw_input('Print reversed string: ')
            print(reversed_string(entered_data))

        elif option == 2:
            entered_data = raw_input('Print uppercased string: ')
            print(uppercase_string(entered_data))

        elif option == 3:
            entered_data = raw_input('Print lowercased string: ')
            print(lowercase_string(entered_data))

        elif option == 4:
            entered_data = raw_input('Print vertical string')
            print(vertical_string(entered_data))

        elif option == 0:
            loop_iterator = option
        else:
            print('Invalid selection!')
    return loop_iterator


mainmenu()
