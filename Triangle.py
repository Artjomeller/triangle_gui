class Triangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def hypotenuse(self):
        return (self.side_a ** 2 + self.side_b ** 2) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.hypotenuse()

    def area(self):
        return 0.5 * self.side_a * self.side_b
