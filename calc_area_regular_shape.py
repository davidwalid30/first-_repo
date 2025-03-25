import math
class Polygon:
    num_of_sides: int = None
    value_of_side: float = None

    def __init__(self,num_of_sides:int = 3,value_of_side:float = 6)-> None:
        self.num_of_sides = float(num_of_sides)
        self.value_of_side = float(value_of_side)

    def get_area (self)-> float:
        main_angle: float = 360 / self.num_of_sides

        secondary_angle: float = 90 - main_angle / 2

        side: float = self.value_of_side * math.sin(secondary_angle) / math.sin(main_angle)

        area_triangle: float = 1 / 2 * math.sin(main_angle) * side**2

        area_P: float = area_triangle * self.num_of_sides

        return area_P
    
# i will choose a pentagone
shape: Polygon = Polygon(5,5)

print(f"the area of this shape is : {shape.get_area()}")