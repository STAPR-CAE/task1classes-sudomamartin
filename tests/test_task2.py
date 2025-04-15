import pytest
import math

from tasks.shape import Shape
from typing import Type


@pytest.fixture
def circle_class():
    try:
        from tasks.task2 import Circle

        return Circle
    except ImportError:
        pytest.fail("Circle class not found.")


def test_circle(circle_class: Type[Shape]):
    circle = circle_class(5)
    assert circle.radius == 5
    assert circle.get_area() == pytest.approx(math.pi * 5**2, rel=1e-9)
    assert circle.get_perimeter() == pytest.approx(2 * math.pi * 5, rel=1e-9)
    assert isinstance(circle, Shape)

    assert circle.diameter == 10

    circle.diameter = 4
    assert circle.radius == 2
    assert circle.diameter == 4

    with pytest.raises(ValueError):
        circle.diameter = -1
