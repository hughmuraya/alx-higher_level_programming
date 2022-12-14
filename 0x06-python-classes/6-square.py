#!/usr/bin/python3
"""Module containing the Square class"""


class Square:
    """The Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing an instance of Square


        Args:
            size (int): The size of the Square instance. Default value is 0.
            position (:obj:'tuple' of int): x, y coordinate offset when
                printing the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Value of 'size'"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        """:obj:'tuple' of int: x, y coordinate offset when printing the square.
        """
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or len(position) is not 2 or
            not isinstance(position[0], int) or
                not isinstance(position[1], int) or position[0] < 0 or
                position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        """Returns the current square area of the instance


        Returns:
           int: Value of 'size'
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square with hashtags using the 'size'. Uses 'position' to
        offset where the printing should begin. The x, y coordinate in
        'position' is the location of the top left corner of the square."""
        if self.__size is not 0:
            for y in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
