
# lambda Function

def square(n):
    return n*n

print(square(5))

# This same task we can do with the help of lambda function.

square = lambda x : x*x
print(square(5))

sum = lambda a,b,c : a+b+c
print(sum(1,2,3))

divide = lambda a,b : a/b
print(divide(100,10))


