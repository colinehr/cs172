"""Unit tests for the Starship class."""

__author__ = 'Peter Drake and Alain Kägi'
from vector import Vector
from starship import Starship

def test_initializer_and_getters():
    ship = Starship('Enterprise', Vector(5.0, 4.0))
    assert ship.name() == 'Enterprise'
    assert str(ship.position) == '<5.0, 4.0>'
    assert str(ship.velocity) == '<0.0, 0.0>'

def test_str():
    ship = Starship('Millenium Falcon', Vector(3.0, 2.0))
    assert str(ship) == 'Millenium Falcon at <3.0, 2.0> moving <0.0, 0.0>'

def test_accelerate_changes_velocity():
    ship = Starship('White Star', Vector(7.0, 1.0))
    ship.accelerate(Vector(3.0, -3.0))
    assert str(ship.velocity) == '<3.0, -3.0>'
    ship.accelerate(Vector(2.0, 9.0))
    assert str(ship.velocity) == '<5.0, 6.0>'

def test_accelerate_does_not_change_position():
    ship = Starship('Red Dwarf', Vector(2.0, 5.0))
    ship.accelerate(Vector(4.0, 2.0));
    assert str(ship.position) == '<2.0, 5.0>'

def test_drift_changes_position():
    ship = Starship('Rocinante', Vector(2.0, 5.0))
    ship.accelerate(Vector(4.0, 2.0))
    ship.drift()
    assert str(ship.position) == '<6.0, 7.0>'
    ship.drift()
    assert str(ship.position) == '<10.0, 9.0>'