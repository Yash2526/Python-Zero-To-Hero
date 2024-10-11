


try:
    a = int(input("Heyy Enter a number: "))
    print(a)

except Exception as e:  
    # If we add this exception then our program wont be crash. It gives an valied exception error.
    print(e)


print("Thank you!")

# If the program crash somehow then thank you will not be print.

