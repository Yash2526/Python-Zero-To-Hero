
# Que.7

# Write a program to print the following star pattern.

'''
*
**
***
****
*****

'''

n = int(input("Ente your number: "))

for i in range(1,n+1):
    print("*"* i , end="")
    print("")