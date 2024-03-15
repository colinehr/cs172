class Vector:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

# new way
vec = Vector(1, 2)

# version 1
def add_vectors(v1: int, v2: int, w1: int, w2: int) -> list[int]:
    return [v1 + w1, v2 + w2]

# version 2
def add_vectors(v: list[int], w: list[int]) -> list[int]:
    v1 = v[0]
    v2 = v[1]
    w1 = w[0]
    w2 = w[1]
    return [v1 + w1, v2 + w2]

# version 3
def add_vectors(v: Vector, w: Vector) -> Vector:
    return Vector(v.x + w.x, v.y + w.y)

v = Vector(
    int(input("x-coordinate of first vector: ")),
    int(input("y-coordinate of first vector: "))
)

x = int(input("x-coordinate of second vector: "))
y = int(input("y-coordinate of second vector: "))
w = Vector(x, y)

new_vec = add_vectors(v, w)

print("sum of vectors: (" + str(new_vec.x) + ", " + str(new_vec.y) + ")")
