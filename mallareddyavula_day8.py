import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:

        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two distinct real roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    if a != 0:
        result = find_roots(a, b, c)
        print(result)
    else:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
except ValueError:
    print("Please enter valid numeric values.")
