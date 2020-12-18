class Polygon:
    name = ''
    sides = 0
    sideLength = 0
    averageAngle = 0
    area = 0
    perimeter = 0

    def __init__(self, name, sides, sideLength):
        self.name = name
        self.sides = sides
        self.sideLength = sideLength
        # self.averageAngle = averageAngle
        # self.area = area
        # self.perimeter = perimeter

    def getName(self):
        pass

    def getPerimeter(self):
        pass

    def getArea(self):
        pass

    def __str__(self):
        s = ''
        s += ' name: ' + str(self.name)
        s += ' sides: ' + str(self.sides)
        s += ' sideLength: ' + str(self.sideLength)
        s += ' averageAngle: ' + str(self.averageAngle)
        s += ' area: ' + str(self.area)
        s += ' perimeter: ' + str(self.perimeter)
        return s

class Triangle(Polygon):
    def __init__(self, sideLength):
        super().__init__(self, 'Triangle', 3, sideLength)

    def getPerimeter(self):
        return self.sideLength * 3

    def getArea(self):
        pass
