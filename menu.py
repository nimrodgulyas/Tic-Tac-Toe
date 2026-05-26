def get_menu_option():
    while True:
        valasztas = input("Give me a number according to the followings: \n1. Human vs Human \n2. Random AI vs Random AI (LATER) \n3. Human vs Random AI (LATER) \nThe number: ").strip()
        if valasztas == '1':
            return 1
        elif valasztas == '2':
            return 2
        elif valasztas == '3':
            return 3
        else:
            print("You didn't give a correct number! Please try again.\n")
