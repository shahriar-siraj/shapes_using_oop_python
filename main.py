class Shape:
    def getHeight(self):
        return self.__height
    
    def getWidth(self):
        return self.__width

    def setHeight(self, height):
        self.__height = height
    
    def setWidth(self, width):
        self.__width = width
    
class Rectangle(Shape):
    def getArea(self):
        return self.getHeight() * self.getWidth()

class Triangle(Shape):
    def getArea(self):
        return ( self.getHeight() * self.getWidth() ) / 2

r = Rectangle()
r.setHeight(3)
r.setWidth(4)
print("The area of the rectangle is:", r.getArea())

t = Triangle()
t.setHeight(3)
t.setWidth(4)
print("The area of the triangle is:", t.getArea())