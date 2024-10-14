# Que.4

# Write a program to find the maximum of the number in a list using the 
# reduce function


from functools import reduce

l = [525,600,985,125,658,245,368,875,164]

def greter(a,b):
    if (a>b):
        return a
    return b

print(reduce(greter, l))


# For Practise...

from functools import reduce

l = [99,58,62,58,45,63,87,123]

def greter(a,b):
    if (a>b):
        return a
    return b

print(reduce(greter, l))
