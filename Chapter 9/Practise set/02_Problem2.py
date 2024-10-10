
# Que.2

# The game {} function in a program lets a user play a game and returns the score as an 
# integer. YOu need to read a file 'Hi-score.text' which is either blanck 
# or contains the previous Hi-score. You need to right a program to update 
# the Hi-score whenever the game{} function break the Hi-score.


import random

def game():
    print("You are playing the game.")

    score = random.randint(1, 100)

    with open("Hiscore.txt") as f: 
        Hiscore = f.read()
        if(Hiscore != ""):
            Hiscore = int(Hiscore)

        else:
            Hiscore = 0

    print(f"Your score: {score}")
    if(score>Hiscore):

        # Write this hiscore to the  file...
        
        with open("Hiscore.txt","w") as f:
            f.write(str(score))


    return score

game()



