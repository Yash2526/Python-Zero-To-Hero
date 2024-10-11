
# Que.3

# Create a class Employee and add salary and increment properties to it.
# Write a method 'salaryafterincrement' method with a @property decorator with a 
# setter which changes the value of increment based on the salary

class Employee:
    salary = 234
    increment = 20

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary * self.increment/100)

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

    
e = Employee()
print(e.SalaryAfterIncrement)
e.SalaryAfterIncrement = 280.8
print(e.increment)