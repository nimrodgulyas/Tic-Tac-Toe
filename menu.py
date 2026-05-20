def get_menu_option():
    human_vs_human = 0
    ai_vs_ai = 0
    human_vs_ai = 0
    valasztas = int(input("Give me a number according to the followings: \n1. Human vs Human \n2. Random AI vs Random AI \n3. Human vs Random AI \n The number:"))
    while valasztas == 1 or 2 or 3:
        if valasztas == 1:
            human_vs_human += 1
            return human_vs_human
            break
        elif valasztas == 2:
            ai_vs_ai += 2
            return ai_vs_ai
            break
        elif valasztas == 3:
            human_vs_ai += 3
            return human_vs_ai
            break
        elif valasztas != 1 or 2 or 3:
            return("You didn't give a correct number!")
print(get_menu_option())