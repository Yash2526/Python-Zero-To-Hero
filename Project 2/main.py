
# Project number.2

# We are going to write a program that generates a random number and
# asks the user to guess it.


import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a != n ):
    a = int(input("Guess the number: "))

    if(a>n):
        print("Lower Number Please.")
        guesses += 1

    elif(a<n):
        print("Higher Number Please.")        
        guesses += 1

print(f"You have Guessed the number {n} correctly in {guesses} attempt")
