#!/usr/bin/python3
""" Module for square class fixed"""


class square():
    """ Square class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instantiation of the square class """

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square method"""
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of my square methid"""

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
