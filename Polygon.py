import math

class Polygon:
    name = ''
    sides = 0
    sideLength = 0

    def __init__(self, name, sides, sideLength):
        self.name = name
        self.sides = sides
        self.sideLength = sideLength

    def getName(self):
        pass

    def getPerimeter(self):
        return self.sideLength * self.sides

    def getArea(self):
        return 'Unknown'

    def getAngle(self):
        return (self.sides - 2) * 180 / self.sides

    def __str__(self):
        return self.name + " (" + str(self.sideLength) + ")"

class Triangle(Polygon):
    def __init__(self, sideLength):
        super().__init__('Triangle', 3, sideLength)

    def getArea(self):
        base = self.sideLength;
        height = (self.sideLength / 2) * math.sqrt(3);
        area = base * height / 2
        return area

class Square(Polygon):
    def __init__(self, sideLength):
        super().__init__('Square', 4, sideLength)

    def getArea(self):
        side = self.sideLength;
        area = side * side
        return area

class Pentagon(Polygon):
    def __init__(self, sideLength):
        super().__init__('Pentagon', 5, sideLength)

class Octagon(Polygon):
    def __init__(self, sideLength):
        super().__init__('Octagon', 8, sideLength)

class Nonagon(Polygon):
    def __init__(self, sideLength):
        super().__init__('Nonagon', 10, sideLength)

triangle = Triangle(10)
square = Square(10)
pentagon = Pentagon(10)
octagon = Octagon(10)
nonagon = Nonagon(10)
for shape in [ triangle, square, pentagon, octagon, nonagon ]:
    print(shape)
    perimeter = shape.getPerimeter()
    angle = shape.getAngle()
    area = shape.getArea()
    print('perimeter: ' + str(perimeter))
    print('angle: ' + str(angle))
    print('area: ' + str(area))
    print()
