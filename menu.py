def mainmenu ():
    loop_iterator = ''
    while loop_iterator == '':
        print ('\nM A I N   M E N U')
        print ('1. Print reversed string')
        print ('2. Print uppercased string')
        print ('3. Print lowercased string')
        print ('0. Exit')
        option = int(raw_input('Select an option: '))
        if option == 1:
            data = raw_input('Print reversed string: ')
            reversed_message = data[::-1]
            print(reversed_message)
        elif option == 2:
            data = raw_input('Print uppercased string: ')
            print(data.upper())
        elif option == 3:
            data = raw_input('Print lowercased string: ')
            print(data.lower())
        elif option == 0:
            loop_iterator = option
        else:
            print('Invalid selection!')
    return loop_iterator
mainmenu()
