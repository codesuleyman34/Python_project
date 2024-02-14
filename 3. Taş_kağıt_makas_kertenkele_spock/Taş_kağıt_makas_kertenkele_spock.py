import random
import operation
import constans
Options = constans.options

while True:
    team2 = random.choice(Options)
    team1 = operation.vote()
    if team1 == constans.exit or team1 == constans.Exit:
        print("Sen bilirsin")
        break
    
    print(f"Seçiminiz: {team1}, Karşı takımın seçimi: {team2}")
    print("--"*20)

    if team1 == team2:
        print("Berabere")
        print("--"*20)
    elif (
        (team1 == constans.rock and team2 == constans.scissors) or
        (team1 == constans.paper and team2 == constans.rock) or
        (team1 == constans.scissors and team2 == constans.paper) or
        (team1 == constans.rock and team2 == constans.lizard) or
        (team1 == constans.lizard and team2 == constans.spock) or
        (team1 == constans.spock and team2 == constans.scissors) or
        (team1 == constans.scissors and team2 == constans.lizard) or
        (team1 == constans.lizard and team2 == constans.paper) or
        (team1 == constans.paper and team2 == constans.spock) or
        (team1 == constans.spock and team2 == constans.rock)
    ):
        print("Kazandınız")
        print("--"*20)
    else:
        print("Kaybettiniz")
        print("--"*20)