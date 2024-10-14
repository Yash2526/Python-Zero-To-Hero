
# Que,3

# Write a program to filter a list of numbers which has divisible of 5

def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a = [98,76,85,25,36,98,77,80,14,27,100]

f = list(filter(divisible5,a))
print(f)