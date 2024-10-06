
# Que.6

# Write a program to calculate the grade of a student from his marks 
# from the following scheme.


a1 =int(input("Enter your marks of sub 1:"))
a2 =int(input("Enter your marks of sub 2:"))
a3 =int(input("Enter your marks of sub 3:"))
a4 =int(input("Enter your marks of sub 4:"))
a5 =int(input("Enter your marks of sub 5:"))
a6 =int(input("Enter your marks of sub 6:"))

grade = (a1+a2+a3+a4+a5+a6)/6

if(grade >=90<=100):
    print("Your grade is Ex.")

elif(grade >=80<=90):
    print("Your grade is A.")

elif(grade >=70<=800):
    print("Your grade is B.")

elif(grade >=60<=70):
    print("Your grade is C.")

elif(grade >=50<=60):
    print("Your grade is D.")

elif(grade <=50):
    print("Your grade is F.")
    

