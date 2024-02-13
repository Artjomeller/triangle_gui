class TriangleModel:
    def __init__(self):
        self.side_a = 0
        self.side_b = 0
        self.hypotenuse = 0
        self.perimeter = 0
        self.area = 0

    def calculate_triangle_properties(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

        self.hypotenuse = (side_a**2 + side_b**2)**0.5
        self.perimeter = side_a + side_b + self.hypotenuse
        self.area = (side_a * side_b) / 2

        return self.hypotenuse, self.perimeter, self.area

    def start_new_calculation(self):
        self.side_a = 0
        self.side_b = 0
        self.hypotenuse = 0
        self.perimeter = 0
        self.area = 0
