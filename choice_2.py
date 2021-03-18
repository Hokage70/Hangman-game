import choice_3


def choice_t():

    t = input("Enter second letter: ")

    if t == "h":
        print("th__")
        print(choice_3.choice_th())

    if t == "o":
        print("t_o_")
        print(choice_3.choice_to())

    if t == "r":
        print("t__r")
        print(choice_3.choice_tr())


def choice_h():

    h = input("Enter second letter: ")

    if h == "t":
        print("th__")
        print(choice_3.choice_ht())

    if h == "o":
        print("_ho_")
        print(choice_3.choice_ho())

    if h == "r":
        print("_h_r")
        print(choice_3.choice_hr())


def choice_o():

    o = input("Enter second letter: ")

    if o == "t":
        print("t_or")
        print(choice_3.choice_ot())

    if o == "h":
        print("_ho_")
        print(choice_3.choice_ho())

    if o == "r":
        print("__or")
        print(choice_3.choice_or())


def choice_r():

    r = input("Enter second letter: ")

    if r == "t":
        print("t__r")
        print(choice_3.choice_rt())

    if r == "h":
        print("_h_r")
        print(choice_3.choice_hr())

    if r == "o":
        print("__or")
        print(choice_3.choice_ro())
