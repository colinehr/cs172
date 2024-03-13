class Vector:
    x: int
    y: int

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
    result = Vector()
    result.x = v.x + w.x
    result.y = v.y + w.y
    return result

v = Vector()
v.x = int(input("x-coordinate of first vector: "))
v.y = int(input("y-coordinate of first vector: "))

w = Vector()
w.x = int(input("x-coordinate of second vector: "))
w.y = int(input("y-coordinate of second vector: "))

new_vec = add_vectors(v, w)

print("sum of vectors: (" + str(new_vec.x) + ", " + str(new_vec.y) + ")")
