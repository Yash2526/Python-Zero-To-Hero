
# Que.1

# Create a class "programmer" for the storing imformation of few programmers
# working at microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Harry",500000,422601)
print(p.name,p.salary,p.pin,p.company) 

r = Programmer("Rohan",25000,422601)
print(r.name,r.salary,r.pin,r.company)
