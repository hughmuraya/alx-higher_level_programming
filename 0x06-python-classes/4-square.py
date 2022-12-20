#!/usr/bin/python3
"""Module containing the Square class"""


class Square:
    """The Square class"""
    def __init__(self, size=0):
        """Initializing an instance of Square


        Args:
            size (int): The size of the Square instance. Default value is 0.
        """
        self.size = size

    @property
    def size(self):
        """int: size of the Square instance"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area of the instance


        Returns:
            int: The square of size
        """
        return self.__size ** 2
