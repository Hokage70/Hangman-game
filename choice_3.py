import choice_4


#  T
def choice_th():
    th = input("Enter third letter:")
    if th == "o":
        print("tho_")
        print(choice_4.choice_tho())

    if th == "r":
        print("th_r")
        print(choice_4.choice_thr())


def choice_to():
    to = input("Enter third letter:")
    if to == "h":
        print("tho_")
        print(choice_4.choice_toh())

    if to == "r":
        print("t_or")
        print(choice_4.choice_tor())


def choice_tr():
    tr = input("Enter third letter:")
    if tr == "h":
        print("th_r")
        print(choice_4.choice_trh())
    if tr == "o":
        print("t_or")
        print(choice_4.choice_tro())


#  H
def choice_ht():
    ht = input("Enter third letter:")
    if ht == "o":
        print("tho_")
        print(choice_4.choice_hto())

    if ht == "r":
        print("th_r")
        print(choice_4.choice_htr())


def choice_ho():
    ho = input("Enter third letter:")
    if ho == "t":
        print("tho_")
        print(choice_4.choice_hot())

    if ho == "r":
        print("_hor")
        print(choice_4.choice_hor())


def choice_hr():
    hr = input("Enter third letter:")
    if hr == "t":
        print("th_r")
        print(choice_4.choice_hrt())

    if hr == "o":
        print("_hor")
        print(choice_4.choice_hor())


#  O
def choice_ot():
    ot = input("Enter third letter:")
    if ot == "h":
        print("tho_")
        return choice_4.choice_oth()

    if ot == "r":
        print("t_or")
        print(choice_4.choice_otr())


def choice_oh():
    oh = input("Enter third letter:")
    if oh == "t":
        print("tho_")
        print(choice_4.choice_oht())

    if oh == "r":
        print("_hor")
        print(choice_4.choice_ohr())


def choice_or():
    orr = input("Enter third letter:")
    if orr == "t":
        print("t_or")
        print(choice_4.choice_ort())

    if orr == "h":
        print("_hor")
        print(choice_4.choice_orh())


#  R
def choice_rt():
    rt = input("Enter third letter:")
    if rt == "h":
        print("th_r")
        print(choice_4.choice_rth())
    if rt == "o":
        print("t_or")
        print(choice_4.choice_rto())


def choice_rh():
    rh = input("Enter third letter:")
    if rh == "t":
        print("th_r")
        print(choice_4.choice_rht())

    if rh == "o":
        print("_hor")
        print(choice_4.choice_rho())


def choice_ro():
    ro = input("Enter third letter:")
    if ro == "t":
        print("t_or")
        print(choice_4.choice_rot())

    if ro == "h":
        print("_hor")
        print(choice_4.choice_roh())
