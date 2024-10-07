
# Que.2

# Write a python program using function to convert the 
# Celsius to Fahrenheit

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F : "))
 
c = f_to_c(f)
print(f"{round(c , 2)} °C")



# Que.3

# How do you prevent a python print() function
# to print a new line at the end.

print("a")
print("b")
print("Yash", end="")
print(" ","&"," ", end="")
print("Kalyani", end="")