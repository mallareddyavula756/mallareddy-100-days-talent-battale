def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y != 0:
        return "On Y-axis"
    elif y == 0 and x != 0:
        return "On X-axis"
    else:
        return "Origin"
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

quadrant = find_quadrant(x, y)
print(f"The point ({x}, {y}) lies in {quadrant}.")
