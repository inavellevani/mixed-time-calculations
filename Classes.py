class Trapezoid:
    def __init__(self, sh_base, lng_base, height):
        self.sh_base = sh_base
        self.lng_base = lng_base
        self.height = height
        self.area = 0

    def __str__(self):
        return f'Short base of trapezoid is {self.sh_base},\nLong base is {self}\nheight is {self.height}'

    def area_calculator(self):
        self.area = ((self.sh_base + self.lng_base) / 2) * self.height

    def __add__(self, other):
        if isinstance(other, Trapezoid):
            return self.area + other.area
        return False

    def __sub__(self, other):
        if isinstance(other, Trapezoid):
            return self.area - other.area
        return False

    def __mod__(self, other):
        if isinstance(other, Trapezoid):
            return self.area // other.area
        return False


class Rectangle(Trapezoid):
    def __init__(self, width, length):
        super().__init__(width, length, length)
        self.width = width
        self.length = length

    def __str__(self):
        return f"Rectangle width is {self.width},\nlength is {self.length}"

    def area_calculator(self):
        self.area = (self.width * self.length)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square's side is {self.side}"

    def area_calculator(self):
        self.area = self.side ** 2
