
import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of the same dimension.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[x / mag for x in self.components])
