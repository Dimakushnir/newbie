def showmenu ():
    print ('\nM A I N   M E N U')
    print ('1. Print reversed string')
    print ('2. Print uppercased string')
    print ('3. Print lowercased string')
    print ('0. Exit')
    selected_option = int(raw_input('Select an option: '))
    return selected_option

def reversed_string (string):
    reversed_message = string[::-1]
    return reversed_message

def uppercase_string ():
    data = raw_input('Print uppercased string: ')
    print(data.upper())

def lowercase_string ():
    data = raw_input('Print lowercased string: ')
    print(data.lower())

def mainmenu ():
    loop_iterator = ''
    while loop_iterator == '':
        option = showmenu()
        if option == 1:
            data = raw_input('Print reversed string: ')
            a = reversed_string(data)
            print(a)

        elif option == 2:
            uppercase_string()

        elif option == 3:
            lowercase_string()

        elif option == 0:
            loop_iterator = option
        else:
            print('Invalid selection!')
    return loop_iterator
mainmenu()
