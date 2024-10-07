
# Que.3

# Write a program to find whether a given number is prime or not .

n = int(input("Enter number: "))

for i in range(2,n):
    if(n%i) == 0:
        print("This Number is not prime")
        break

else:
    print("This is Prime Number")

 