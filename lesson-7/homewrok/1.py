import math as m
from pickle import GLOBAL


class Vektor:
    def __repr__(self):
        return f"Vektor{self.kordinatalar}"

    def __init__(self,*args):
        self.kordinatalar = args
    def __add__(self, other):
        if len(self.kordinatalar) != len(other.kordinatalar):
            raise ValueError("Kordinatalar soni teng bo'lishi kerak")
        else:
            return Vektor(*(self.kordinatalar[i] + other.kordinatalar[i] for i in range(len(self.kordinatalar))))
    def __sub__(self, other):
        if len(self.kordinatalar) != len(other.kordinatalar):
            raise ValueError("Kordinatalar soni teng bo'lishi kerak")
        else:
            return Vektor(*(self.kordinatalar[i] - other.kordinatalar[i] for i in range(len(self.kordinatalar))))
    def __mul__(self, other):
        if isinstance(other, Vektor):
            if len(self.kordinatalar) != len(other.kordinatalar):
                raise ValueError("Kordinatalar soni teng bo'lishi kerak")
            return sum(self.kordinatalar[i] * other.kordinatalar[i] for i in range(len(self.kordinatalar)))
        elif isinstance(other, (int, float)):
            return Vektor(*(other * i for i in self.kordinatalar))
        else:
            raise ValueError("Noto'g'ri ko'paytirish turi")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vektor(*(other * i for i in self.kordinatalar))
        else:
            raise ValueError("Noto'g'ri ko'paytirish turi")

    def magnitude(self):
        return m.sqrt(sum((i)**2 for i in self.kordinatalar))
    def normalize(self):
        b = m.sqrt(sum((i) ** 2 for i in self.kordinatalar))
        return Vektor(*("{:.3f}".format(self.kordinatalar[i]/b) for i in range(len(self.kordinatalar))))


v1 = Vektor(1,2,3)
v2 = Vektor(4,5,6)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
v5 = v1 * 3
print(v5)
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)





