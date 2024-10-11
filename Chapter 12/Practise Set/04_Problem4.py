
# Que.4

# Write a program to display a/b where a and b are integers.
# if b=0 display infinte by handling the ZeroDivisionError


try:
    a = int(input("Enter a number a: "))
    b = int(input("Enter a number b: "))

    print(f"The Division of a/b is {a/b}")

except ZeroDivisionError as v:
    print("Infinite")
