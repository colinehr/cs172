"""Unit tests for the Vector class."""

__author__ = 'Peter Drake and Alain Kägi'

from vector import Vector

import pytest

EPSILON = 0.0001

def test_getters():
    v = Vector(8.0, 5.0)
    assert v.x == 8.0
    assert v.y == 5.0
    v.x = -2.0
    v.y = 10.0
    assert v.x == -2.0
    assert v.y == 10.0

def test_cant_set_x():
    v = Vector(8.0, 5.0)
    with pytest.raises(AttributeError) as _:
        v.x = 2

def test_cant_set_y():
    v = Vector(8.0, 5.0)
    with pytest.raises(AttributeError) as _:
        v.y = 3

def test_equal():
    assert Vector(1.0, 2.0) == Vector(1.0, 2.0)
    assert Vector(7.0, 7.0) != Vector(7.0, 3.0)

def test_add():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    assert str(a + b) == '<5.0, 8.0>'

def test_add_immutability():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    a + b
    assert str(a) == '<1.0, 2.0>'
    assert str(b) == '<4.0, 6.0>'

def test_subtract():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    assert str(a - b) == '<-3.0, -4.0>'

def test_dot_product():
    a = Vector(1.0, 2.0)
    b = Vector(4.0, 6.0)
    assert str(a * b) == 16.0

def test_scalar_product():
    a = Vector(1.0, 2.0)
    assert str(a * 3.0) == '<3.0, 6.0>'

def test_distance():
    a = Vector(0.0, 3.0)
    b = Vector(4.0, 0.0)
    assert a.distance_to(b) == pytest.approx(5.0, rel = EPSILON)