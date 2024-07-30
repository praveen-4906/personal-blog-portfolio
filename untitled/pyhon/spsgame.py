import random

sign = ["stone","paper","scissor"]
computerscore = 0
userscore = 0

def play (name) :
    global computerscore
    global userscore
    i = 0
    while i < 10 :
        computerpick = random.choice(sign)
        userpick = input("Enter your pick : ")
        print("The computer pick was : ",computerpick)
        if userpick == computerpick :
            print("DRAW")
            continue
        if userpick == "stone" and computerpick == "scissor" :
            print("YOU WON !")
            userscore += 1
        elif userpick == "paper" and computerpick == "stone" :
            print("YOU WON !")
            userscore += 1
        elif userpick == "scissor" and computerpick == "paper" :
            print("YOU WON !")
            userscore += 1
        else :
            print("YOU LOST !")
            computerscore += 1
        i = i + 1
    print("\nYOUR SCORE     : ",userscore)
    print("COMPUTER SCORE : ",computerscore)
    if userscore > computerscore :
        print("YOU WON THE MATCH !!!!")
    elif computerscore > userscore :
        print("SORRY YOU LOST THE MATCH")
    file = open("highscores.txt", "a")
    score = str(userscore)
    file.write(name + " - " + score + '\n')
    file.close()

def main () :
    print("WELCOME TO STONE PAPER SCISSOR GAME")
    choice = int(input("1. Play a new game\n2.View highscores\nEnter your choice : "))
    if choice == 1 :
        name = input("Enter your name : ")
        print("You have 10 chances to play")
        choice = input("Do you wish to play (y/n) : ")
        if choice == 'y' :
            play(name)
    else :
        file = open("highscores.txt","r")
        print(file.read())
        file.close()
        choice = input("Continue playing (y/n) ? : ")
        if choice == 'y' :
            main()

main()