
# Que.2

# A list contains the multiplication table of 7.
# Write a program to convert it to vertical string of the same number

n = int(input("Enter a number: "))

table = [str(n*i) for i in range(1,11)]  # Here make sure about str.

s = "\n".join(table)
print(s)

