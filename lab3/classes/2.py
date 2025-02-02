class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length ** 2
a = float(input("a:"))
square1=Square(a)
print("Area1:",mysquare.area())
shape1=Shape()
print("Area2:",myshape.area())