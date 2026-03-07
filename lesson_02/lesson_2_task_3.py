import math

def square(side):
    area = side * side
    
    if isinstance(side, float):
        area = math.ceil(area)
    
    return area
print(square(4.9))