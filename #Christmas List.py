christmas_list = "Books Journal Art Calander Candles Technology Desk Monitor LEDLights"
real_list = christmas_list.split()

lesly_list = real_list[0:5]
adrian_list = real_list[-4:]

while True:
    initial_response = input("Want to add something to your list, Lesly? ").lower()
    if initial_response == "yes":
        #while True:
        lesly_list.append(str(input("What would you like to add? ")))
        print("Great! Here is your new list:", lesly_list) 
        something_else = str(input('Want to add something else? '))
        if something_else == 'yes':
            lesly_list.append(str(input('Okay, what would you like to add now? ')))
            (print('Here is your new list!', lesly_list))
            if input('Anything else you want to add? ') == 'yes':
                continue
            else:
                print('Thank you! Good-bye.')
                break
        elif something_else == 'no':
            print('Thank you! Good-bye.')
            break
        else:
            print('Invalid entry.')
            continue
    elif initial_response == "no":
        print('Fine then. BYE FELICIA!')
        break
    else:
        print('Type "Yes" or "No" only.')
        continue

house_addresses = {'home1':{'address': '43548',
                            'street': 'Virginia',
                            'state': 'California',
                            'Zip Code': '92211'},
                    'atomic':{'number': 'HE',
                                'atomic number': 1}
                    }
new = house_addresses['home1']
#print(max(sorted(new)))

