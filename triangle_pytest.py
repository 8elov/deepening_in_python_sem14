import pytest
from triangle import Triangle, InvalidTriangleError, TriangleTypeNotFoundError


def test_valid_triangle_classification():
    """Valid triangle classification."""
    triangle = Triangle(3, 4, 5)
    assert triangle.classify_triangle() == "Разносторонний треугольник"


def test_invalid_triangle_creation():
    """Invalid triangle creation."""
    with pytest.raises(InvalidTriangleError):
        triangle = Triangle(1, 2, 3)


def test_equilateral_triangle_classification():
    """Equilateral triangle classification."""
    triangle = Triangle(6, 6, 6)
    assert triangle.classify_triangle() == "Равносторонний треугольник"


def test_invalid_triangle_classification():
    """Invalid triangle classification"""
    with pytest.raises(TriangleTypeNotFoundError):
        triangle = Triangle(2, 2, 5)


def test_zero_or_negative_sides():
    """Zero or negative side values"""
    with pytest.raises(InvalidTriangleError):
        triangle = Triangle(-1, 2, 3)
    with pytest.raises(InvalidTriangleError):
        triangle = Triangle(0, 4, 5)


def test_sum_of_two_sides_equals_third():
    """Sum of two sides equals the third side"""
    with pytest.raises(InvalidTriangleError):
        triangle = Triangle(2, 3, 5)


def test_non_integer_sides():
    """Non-integer side values"""
    with pytest.raises(ValueError):
        triangle = Triangle(1.5, 2, 3)
