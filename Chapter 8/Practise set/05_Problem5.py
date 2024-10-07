
# Que.5

# Write a python finction to print n lines of the following pattern.

n = int(input("Enter number: "))

def pattern(n):
    if(n==0):
        return
    
    print("*"* n)
    pattern(n-1)

pattern(n)