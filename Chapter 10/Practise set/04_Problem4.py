
# Que.4

# Add a staticmethod in problem 2 to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n = n

    @staticmethod   # Here we use the staticmethod.
    def greet():
        print("Hello Everyone!")

    def square(self):
        print(f"The Square is: {self.n*self.n}")


a = Calculator(5)
a.greet()
a.square()