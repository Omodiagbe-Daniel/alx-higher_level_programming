#!/usr/bin/python3
"""a class rectangle"""


class Rectangle:
    """a class based on 7-rectangle"""

    number_of_instances = 0
    print_symbol = '#'
    """public class attribute"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = ''
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                rect += (str(self.print_symbol) * self.__width)
                if i != self.__height - 1:
                    rect += ("\n")
            return (rect)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect1 = rect_1.area()
        rect2 = rect_2.area()
        if rect1 >= rect2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """classmethod"""

        width = size
        height = size
        return cls(width, height)
