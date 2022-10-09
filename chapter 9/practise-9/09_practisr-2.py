def game():
    return 500

score = game()
with open('chapter 9/highscore.txt') as f:
    highscore = f.read()

if highscore=='':
    with open('chapter 9/highscore.txt', 'w') as f:
        f.write(str(score))

elif int(highscore) < score:
    with open('chapter 9/highscore.txt', 'w') as f:
        f.write(str(score))

else:
    pass