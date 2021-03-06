#Create a shopping list.
shopping_list = []
def shopping_program():
    while True:
        print("""
        Type: "HELP" for help. "SHOW" to show cart. "QUIT" to exit app. "CHECKOUT" to check out.
        What items would you like to add to you list?"
        """)
        new_item = input("Next item: ")
        if new_item == "HELP":
            back = input('These are instructions. Type "BACK" to return to the main screen. ')
            if back == "BACK":
                continue
            else:
                print("Invalid entry")
        elif new_item == "SHOW":
            index = 1
            for item in shopping_list:
                print("{}. {}".format(index, item))
                index += 1
            continue
        elif new_item == "QUIT":
            back = input("Are you sure you want to quit? 'YES' or 'NO' ")
            if back == "YES":
                break
            elif back == "NO":
                continue
        elif new_item == "CHECKOUT":
            check_out()
        else:
            shopping_list.append(new_item)

def check_out():
    while True:
        print("""
        This is your shopping cart.
        Type \"BACK\" to return to main menu.
        """)
        back = input("Did you want to check out? 'YES' or 'BACK' ")
        if back == "BACK":
            shopping_program()
        elif back == "YES":
            print("Thank you!")
            break
        else:
            print("Invalid entry.")
            continue
shopping_program()
check_out()