#!/usr/bin/python3

class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance with the given size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for retrieving the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for setting the position."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(val, int) for val in value) or \
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' characters and position."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

