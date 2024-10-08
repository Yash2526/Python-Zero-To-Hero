
import random

'''    
1 for snake 
-1 for water
0 for gun
'''

# Computer randomly chooses -1, 0, or 1
computer = random.choice([-1, 0, 1])

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Dictionaries to map inputs
youDict = {"s": 1, "w": -1, "g": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Check if the input is valid
if youstr not in youDict:
    print("Invalid input. Please choose 's', 'w', or 'g'.")
else:
    you = youDict[youstr]
    
    # Display choices
    print(f"You chose {reversedDict[you]}\nComputer chose {reversedDict[computer]}")

    # Check for a draw
    if computer == you:
        print("It's a draw")

    # Check for win or loss
    else:
        if (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
            print("You win!")
        else:
            print("You lose!")
