

# Raising the Error

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if (b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divied number by zero.")

print(f"The Division of a/b is {a/b}")

