from tasks.shape import Shape
import math

"""
## Exercise 2: Properties
In this exercise, you'll practice using properties
by implementing a `Circle` class.

property getter can be implemented using the `@property` decorator.
property setter can be implemented using the `@property_name.setter` decorator. (for example, `@diameter.setter`)
"""


# Implement the Circle class here
class Circle(Shape):
    pass
    # implement __init__ method with protected _radius parameter
    # implement get_area method, use math.pi for pi
    # implement get_perimeter method, use math.pi for pi
    # implement __str__ method
    # implement diameter property
    # implement diameter property setter with validation
    #     raise ValueError("Diameter must be positive") if diameter is negative


def main():
    # Test your implementation
    # Uncomment the following code when you're ready to test
    # Run main.py to see the output

    print("Testing tasks/task2.py")

    # circle = Circle(5)
    # print(circle)  # Should display circle info
    # print(f"Radius: {circle._radius}")
    # print(f"Area: {circle.get_area():.2f}")
    # print(f"Circumference: {circle.get_perimeter():.2f}")
    # print(f"Diameter: {circle.diameter}")

    # # Update via diameter property
    # circle.diameter = 14
    # print(f"After changing diameter to 14:")
    # print(f"Radius is now: {circle._radius}")
    # print(f"Area is now: {circle.get_area():.2f}")

    # # Test validation
    # try:
    #     circle.diameter = -2
    #     print("Error: Setting negative diameter should raise an exception")
    # except ValueError as e:
    #     print(f"Correctly caught error: {e}")

    print("Completed tasks/task2.py")
