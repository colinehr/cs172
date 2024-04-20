import pytest
import math
from complex import Complex


def complex_eq(z: Complex, w: Complex):
    return z.real == pytest.approx(w.real) and z.imaginary == pytest.approx(w.imaginary)


def test_real():
    z = Complex(3.0, 1.0)
    assert z.real == 3.0


def test_imaginary():
    z = Complex(3.0, 1.0)
    assert z.imaginary == 1.0


def test_str():
    z = Complex(3.0, 1.0)
    assert str(z) == "3.0 + 1.0i"


def test_str_negative():
    z = Complex(3.0, -1.0)
    assert str(z) == "3.0 - 1.0i"


def test_eq():
    z = Complex(3.0, 1.0)
    w = Complex(3.0, 1.0)
    assert z == w


def test_neq():
    z = Complex(3.0, 1.0)
    w = Complex(3.0, 2.0)
    assert z != w


def test_add():
    z = Complex(3.0, 1.0)
    w = Complex(1.0, 2.0)
    assert z + w == Complex(4.0, 3.0)


def test_sub():
    z = Complex(3.0, 1.0)
    w = Complex(1.0, 2.0)
    assert z - w == Complex(2.0, -1.0)


def test_neg():
    z = Complex(3.0, 1.0)
    assert -z == Complex(-3.0, -1.0)


def test_mul():
    z = Complex(3.0, 1.0)
    w = Complex(1.0, 2.0)
    assert z * w == Complex(1.0, 7.0)


def test_abs():
    z = Complex(3.0, 1.0)
    assert abs(z) == math.sqrt(10)


def test_div():
    z = Complex(3.0, 1.0)
    w = Complex(1.0, 2.0)
    result = z / w
    assert result.real == pytest.approx(1)
    assert result.imaginary == pytest.approx(-1)