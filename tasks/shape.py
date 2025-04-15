"""
This module defines an abstract base class for shapes.
This is a template for creating specific shape classes like Circle, Rectangle, etc.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Base abstract class for all shapes."""

    @abstractmethod
    def get_area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def get_perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

    def __str__(self):
        """Return a string representation of the shape."""
        return f"{self.__class__.__name__}"
