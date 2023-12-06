class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __len__(self):
        return int((self.x**2 + self.y**2 + self.z**2)**(1/2))
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return "Складывать можно только вектор с вектором"
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return "Вычитать можно только вектор из вектора"
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        return ("Умножать можно только вектор на число или вектор")
    
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __pow__(self, power):
        return Vector(self.x**power, self.y**power, self.z**power)


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
# print(v1)
# print(len(v1))

# v3 = v1 + v2
# print(v3)

# v4 = v1 - v2
# print(v4)

# v5 = v1 * 2
# print(v5)

# v6 = v1 * v2
# print(v6)

# print(v1 == v2)
# print(v1 != v2)

# v7 = v1 ** 2
# print(v7)

# v1 += v2
# print(v1)

# v2 -= v1
# print(v2)

# v3 *= 2
# print(v3)
