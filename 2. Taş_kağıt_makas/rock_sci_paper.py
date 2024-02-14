import random

gamer_choice = 0
computer_choice = 0


def get_gamer_choice():
    gamer_choice = int(input("Taş (1), Kağıt (2), Makas (3) : "))

def get_computer_choice():
    computer_choice = random.randint(1, 3)

def computer_choise_rock():
    return computer_choice == 1

def computer_choise_paper():
    return computer_choice == 2

def computer_choise_sciss():
    return computer_choice == 3

def gamer_choise_rock():
    return gamer_choice == 1

def gamer_choise_paper():
    return gamer_choice == 2

def gamer_choise_sciss():
    return gamer_choice == 3

def play_game():
    get_computer_choice()
    
    if gamer_choice == computer_choice:
        print("berabere")
    elif gamer_choise_rock:
        if computer_choise_paper:
            print("Bilgisayar kazandı")
        else:
            print("Kazandınız")
    elif gamer_choise_paper:
        if computer_choise_sciss:
            print("Bilgisayar kazandı")
        else:
            print("Kazandınız")
    elif gamer_choise_sciss:
        if computer_choise_rock:
            print("Bilgisayar kazandı")
        else:
            print("kazandınız")