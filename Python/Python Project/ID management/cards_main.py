#! /usr/bin/python3
import cards_tools

while True:
    #show the interface menu
    cards_tools.menu_interface()
    choose_function=input("please choose the function:")
    print("your choice is [%s]" %choose_function)

    # 1,2,3 choice
    # 0 quit
    # others, warning to choose the correct function
    if choose_function in ["1","2","3"]:

        if choose_function=='1':

            cards_tools.add_ID()

        elif choose_function=='2':

            cards_tools.show_all()

        elif choose_function=='3':

            cards_tools.search_ID()

    elif choose_function=='0':
        print("Goodbye")
        break
    else:
        print("please choose the correct function: ")
        continue
