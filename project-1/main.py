 #==================================================ROCK  PAPER  SCISSOR  GAME===========================================================

import random

def RPS(comp, you):
    if comp == you:
        return "tie"
    if comp == "r":
        if you == "s":
            return False
        elif you == "p":
            return True
    

    if comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True

    if comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True




rn = random.randint(1,3)
if rn == 1:
    comp = "r"
elif rn == 2:
    comp = "p"
    
elif rn == 3:
    comp = "s"

you = input("Enter you Turn among rock(r) paper(p) or scissor(s)")

if you == "r" or you == 's' or you == 'p':

    a = RPS(comp,you)

    print(f'computer chose {comp}')
    print(f'You chose {you}')

    if a == 'tie':
            print('The game is Tie..................:?')
    elif a == True:
        print('You Won.......!')

    else:
        print('You lost...........:(')


else:
    print("chose among r,p and s")








