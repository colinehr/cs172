import math


class Complex:
    _real: float
    _imaginary: float

    def __init__(self, real: float, imaginary: float):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self) -> float:
        return self._real
    
    @property
    def imaginary(self) -> float:
        return self._imaginary
    
    def conjugate(self) -> "Complex":
        return Complex(self.real, -self.imaginary)
    
    def __add__(self, other: "Complex") -> "Complex":
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __neg__(self) -> "Complex":
        return Complex(-self.real, -self.imaginary)
    
    def __sub__(self, other: "Complex") -> "Complex":
        return self + -other
    
    def __mul__(self, other: "Complex") -> "Complex":
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(real, imaginary)
    
    def __truediv__(self, other: "Complex") -> "Complex":
        inv = Complex(1 / abs(other) ** 2, 0) * other.conjugate()
        return self * inv
    
    def __abs__(self) -> float:
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)
    
    def __eq__(self, other: "Complex") -> bool:
        real_eq = abs(self.real - other.real) < 1e-6
        imag_eq = abs(self.imaginary - other.imaginary) < 1e-6
        return real_eq and imag_eq
    
    def __str__(self) -> str:
        if self.imaginary >= 0:
            return str(self.real) + " + " + str(self.imaginary) + "i"
        else:
            return str(self.real) + " - " + str(-self.imaginary) + "i"