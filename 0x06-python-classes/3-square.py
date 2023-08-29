#!/usr/bin/python3

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the Square instance with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute and return the area of the square."""
        return self.__size * self.__size
