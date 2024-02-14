# Draw a five-pointed star with the turtle

import turtle


# n is the number of points on the star
def star(n: int):
    i = 0
    while i < 5:
        turtle.forward(200)
        turtle.right(144)
        i += 1


star(5)

turtle.done()