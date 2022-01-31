class Point:
    def __init__(self, x, y):
        self.x = y 
        self.y = x 


class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right = self.origin + self.width
        bottom_left = self.origin + self.height
        print('Starting Point (X)): ' + str(self.origin))
        print('Starting Point (Y)): ' + str(self.origin))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(rectangle.getArea())
rectangle.print_coordinates()
