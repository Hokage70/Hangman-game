import choice_2
#  start
def start():

    print("Hi, Welcome to Hangman")
    x = input("Would you like to play?")
    if x ==("yes"):
        print("Great!  Hints:\n 1. It is a Norse God ")
    if x == ("no"):
        print ("Well, fuck you then.")
        print(start())

    thor = input("Type first letter: ")

#  T
    if thor == ("t"):
        print("t___")
        print (choice_2.choice_t())

#  H
    if thor == ("h"):
        print("_h__")
        print(choice_2.choice_h())

#  O
    if thor == ("o"):
        print("__o_")
        print(choice_2.choice_o())
#  R
    if thor == ("r"):
        print("___r")
        print(choice_2.choice_r())

start()
