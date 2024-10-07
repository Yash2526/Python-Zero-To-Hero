
# Que.9

# Write a program to printing multiplication table of n using for loops in reversed order


n = int (input("Enter your number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")  # For Simple Table Multiplication..

print("End of Table")

for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")  # For Reverse table Multiplication..

'''
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50 # Do reverse of it..

'''
