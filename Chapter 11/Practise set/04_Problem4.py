
# Que.4

# Write a class Complex to represent complex number along with overloded
# operators + and * which adds and multiplies them

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)


# Example usage
c1 = Complex(1, 2)
c2 = Complex(3, 4)
c3 = c1 * c2
print(f"Multiplication: ({c3.r}, {c3.i})")  # Output: Multiplication: (-5, 10)
