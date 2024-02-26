import graphics as g

width = 800
height = 800

x_start = 500
y_start = 300
radius = 30

dx = 2
dy = 3

# Create a graphics window
win = g.GraphWin("Bouncing Ball", width, height)
win.setBackground("white")

# Create a circle
ball = g.Circle(g.Point(x_start, y_start), radius)
ball.setFill("black")
ball.draw(win)

# Move the ball
while win.checkMouse() is None:
    x = ball.getCenter().getX()
    y = ball.getCenter().getY()
    if (x >= width - radius) or (x <= radius):
        dx = -dx
    if (y >= width - radius) or (y <= radius):
        dy = -dy
    ball.move(dx, dy)

# Close the window
win.close()
