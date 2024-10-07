
# Que.1

# Write a program to  print multiplication table of given number 

# 'using for loop'


n = int(input("Enter number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

print("End of for loop")


# 'Using While loop'

p = int(input("Enter number: "))

i = 1

while(i<11):
    print(f"{n}x{i} = {n*i}")
    i += 1
