# Default Parameter value...

def goodDay(name,ending="Thank you"): 
   
    print(f"Good Day, {name}")          
   
    print(ending)

goodDay("Harry","Thanks")  # It will print Supplied Value i.e Thanks.

goodDay("Yash")  # It will basically print the Bydefault Value "Thank You".

# For Ex.

def greet(name, surname='Stranger'):
    print(f"Hey i'am, {name}")
    print(surname)

greet("Yash","Bharitkar")
greet("Yash")



