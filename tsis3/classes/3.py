class Shape:
    def __init__(self):
        area = 0
class Rectangle(Shape):
    def __init__(self):
        l = int(input())
        w = int(input())
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width
rect = Rectangle()
print(rect.area())