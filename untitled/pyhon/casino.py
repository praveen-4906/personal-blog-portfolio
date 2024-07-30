# Gambling Game

import random

slots = [" Python "," Java "," C++ "]
amount = 1000
betamount = 0

def lose () :
    print("SORRY YOU LOSE")
    choice = input("Do you wish to play again (y/n) : ")
    if choice == 'y' :
        main()
    else :
        exit()

def play (betamount) :
    global amount
    amt=0
    slot1 = random.choice(slots)
    slot2 = random.choice(slots)
    slot3 = random.choice(slots)
    print("Your luck is ",slot1,slot2,slot3)
    if slot1 != slot2  and slot2!= slot3 and slot1!=slot3:
        print("case 1 notequal")
        amount = amount - betamount
    elif slot1 == slot2 and  slot2==slot3 :
        print("case 2 3 equal")
        amount = amount + betamount
    else :
        print("case 3 2 equal")
        amount = amount + betamount/2
    print("Your current amount is ",amount)
    if amount <= 0 :
        lose()
    choice = input("Do you want to place bet or withdraw (y/n) : ")
    if choice == 'y' :
        getbet()
    else :
        withdraw()

def withdraw () :
    print("YOU HAVE WON ",amount," COINS")
    choice = input("Do you wish to play again (y/n) : ")
    if choice == 'y' :
        main()
    else :
        exit()

def getbet () :
    print("Your current amount is : ",amount)
    choice = input("Do you wish to play or withdraw (y/n) : ")
    if choice == 'y' :
        betamount = int(input("Enter the bet amount : "))
        if betamount > amount :
            print("Enter a betamount less than amount")
            getbet()
        else :
            choice = input("Do you wish to continue (y/n) : ")
            if choice == 'y':
                play(betamount)
    else :
        withdraw()

def main () :
    name = input("Enter your name : ")
    print("Welcome ",name)
    print("You have 1000 coins to start with")
    choice = input("Do you wish to play (y/n) : ")
    if choice == 'y' :
        getbet()

main()
