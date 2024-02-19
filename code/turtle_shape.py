# Draw a five-pointed star with the turtle

import turtle


# n is the number of points on the star (odd n only)
def star(n: int):
    i = 0
    while i < n:
        turtle.forward(200)
        turtle.right(360 * 2/n)
        i += 1


def spiral(length: float, angle: int):
    if length <= 1:
        return
    turtle.forward(length)
    turtle.left(angle)
    spiral(length * 0.95, angle)


spiral(200, 80)

turtle.done()