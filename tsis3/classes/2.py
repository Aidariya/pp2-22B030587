class Shape:
    def __init__(self):
        area = 0
class Square(Shape):
    def __init__(self):
        l = int(input())
        self.length = l
    def area(self):
        return self.length*self.length
sqr = Square()
print(sqr.area())