
# Que.4

# Write a program to find wether a given username contains less than 10 characters or not.

a = input("Enter username: ")

if(len(a)<=10):
    print("This username contains less then 10 characters:",len(a))

else:
    print("This username contains more then 10 characters:",len(a))

