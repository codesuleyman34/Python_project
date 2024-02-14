import random

roll_list = []


def roll_dice(quantity):
    for i in range(quantity):
        roll = random.randint(1, 6)
        roll_list.append(roll)
        print("Attığınız zar :", roll, "geldi")



def print_list():
    print("Tüm zarlar:")
    for i in range(len(roll_list)):
        print((i + 1), ". zar : ", roll_list[i])