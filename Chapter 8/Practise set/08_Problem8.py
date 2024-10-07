
# Que.8

# Write a python function to print multiplication table of a given number

m = int(input("Enter number: "))

def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")

multiply(m)