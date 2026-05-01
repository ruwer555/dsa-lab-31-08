import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides


# ПОЗИТИВНЫЕ ТЕСТЫ 
def test_create_equilateral():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9


def test_create_isosceles():
    t = Triangle(5, 5, 8)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 18


def test_create_nonequilateral():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12


def test_float_sides():
    t = Triangle(0.5, 0.6, 0.7)
    assert t.triangle_type() == "nonequilateral"
    assert round(t.perimeter(), 2) == 1.8


# НЕГАТИВНЫЕ ТЕСТЫ
def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 5, 5)


def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 3, 4)


def test_inequality():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 3)


def test_inequality2():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(10, 2, 3)


def test_invalid_str():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 5, 5)


def test_invalid_none():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(None, 4, 5)