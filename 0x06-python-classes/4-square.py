#!/usr/bin/python3

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the Square instance with the given size."""
        self.size = size

    @property
    def size(self):
        """Getter method for retrieving the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size * self.__size
