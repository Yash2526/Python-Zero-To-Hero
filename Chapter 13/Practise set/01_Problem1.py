
# Que.1

# Write a program to input name,marks and phone number of a 
# student and formate it using the formate function like below.

# "The name of the student is  Harry, his marks are 75 and 
# phone number is 9595564023 "


# For this Que we are using format function

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Enter phone number: "))

s ="The name of the student is {} his marks are {} and phone number is {}".format(name,marks,phone)

print(s)

