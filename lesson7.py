class Vector2D:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

v1 = Vector2D(3,4)
v2 = Vector2D(1,2)

v3 = v1 + v2

print(v3)
print(v1 == v2)
print(len(v1))
print(repr(v1))