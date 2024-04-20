import math


class Complex:
    _r: float
    _theta: float

    def __init__(self, real: float, imaginary: float):
        self._r = math.sqrt(real ** 2 + imaginary ** 2)
        self._theta = math.atan2(imaginary, real)

    @property
    def real(self) -> float:
        return self._r * math.cos(self._theta)
    
    @property
    def imaginary(self) -> float:
        return self._r * math.sin(self._theta)
    
    def conjugate(self) -> "Complex":
        return Complex(self.real, -self.imaginary)
    
    def __add__(self, other: "Complex") -> "Complex":
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __neg__(self) -> "Complex":
        return Complex(-self.real, -self.imaginary)
    
    def __sub__(self, other: "Complex") -> "Complex":
        return self + -other
    
    def __mul__(self, other: "Complex") -> "Complex":
        real = self._r * other._r * math.cos(self._theta + other._theta)
        imaginary = self._r * other._r * math.sin(self._theta + other._theta)
        return Complex(real, imaginary)
    
    def __truediv__(self, other: "Complex") -> "Complex":
        real = self._r / other._r * math.cos(self._theta - other._theta)
        imaginary = self._r / other._r * math.sin(self._theta - other._theta)
        return Complex(real, imaginary)
    
    def __abs__(self) -> float:
        return self._r
    
    def __eq__(self, other: "Complex") -> bool:
        real_eq = abs(self.real - other.real) < 1e-6
        imag_eq = abs(self.imaginary - other.imaginary) < 1e-6
        return real_eq and imag_eq
    
    def __str__(self) -> str:
        if self.imaginary >= 0:
            return str(self.real) + " + " + str(self.imaginary) + "i"
        else:
            return str(self.real) + " - " + str(-self.imaginary) + "i"