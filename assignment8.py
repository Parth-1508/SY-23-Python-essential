import math

def calculate_area(*args):
    """
    1 argument: Circle (radius)
    2 arguments: Rectangle (length, width)
    3 arguments: Triangle (base, height, shape_name) - 3rd is just a dummy to differentiate
    """
    if len(args) == 1:
        radius = args[0]
        area = math.pi * (radius ** 2)
        print(f"Area of Circle: {area:.2f}")
    
    elif len(args) == 2:
        length, width = args
        area = length * width
        print(f"Area of Rectangle: {area:.2f}")
        
    elif len(args) == 3:
        base, height, _ = args
        area = 0.5 * base * height
        print(f"Area of Triangle: {area:.2f}")
    
    else:
        print("Invalid number of arguments provided.")

# Polymorphic function calls
calculate_area(5)                   # Circle: radius 5
calculate_area(4, 6)                # Rectangle: length 4, width 6
calculate_area(4, 5, 'triangle')    # Triangle: base 4, height 5