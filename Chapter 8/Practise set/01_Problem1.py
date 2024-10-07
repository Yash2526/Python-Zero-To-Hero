
# Que.1

# Write a program using function to find greatest of three numbers.


def gretest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    

a = 25
b = 50
c = 1000


print(gretest(a,b,c))