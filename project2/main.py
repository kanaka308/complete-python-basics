#**************************************The Perfect Guess*********************************************

import random

randnumber = random.randint(1,100)


userGuess = None
guesses = 0

while(userGuess != randnumber):



    userGuess = int(input("Guess your number\n"))
    guesses += 1

    if(userGuess == randnumber):
        print('you guessed right!..')

    else:
        if(userGuess>randnumber):
            print('the number is samller')
        else:
            print('the number is greater')

print(f'You guessed in {guesses} guesses')
with open('project2/highscore.txt', 'r') as f:
    highScore = int(f.read())

if(guesses<highScore):
    print("you broke the highscore!...")
    with open('project2/highscore.txt', 'w') as f:
        f.write(str(guesses))

        



    