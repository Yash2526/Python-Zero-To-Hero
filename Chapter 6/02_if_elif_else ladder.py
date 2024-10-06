 

# if elif else ladder


a =int(input("Enter your age: "))


# This is 1st statement of 'if'....
if(a%2==0):
    print("a is even.")
# End of statment 1st...


# This is an 2nd statement of 'if'....

if(a>=18):
    print("Hey Welcome you are above the age of consent. ")
    print("You are good to go.")

elif(a<0):
    print("Sorry! You are entering a invalid age.")

elif(a==0):
    print("You are entering 0,which is not a valid age.")

else:
    print("Sorry! You are below the age of consent.")
    print("So you can not go.")

print("Thank you!")
