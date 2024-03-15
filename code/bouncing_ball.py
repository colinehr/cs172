import graphics as g


class Ball:
    x: float
    y: float
    radius: float
    dx: float
    dy: float
    circle: g.Circle

    def __init__(self, x_start: float, y_start: float, radius: float, dx: float, dy: float):
        self.x = x_start
        self.y = y_start
        self.radius = radius
        self.dx = dx
        self.dy = dy
        self.circle = g.Circle(g.Point(self.x, self.y), self.radius)

    def draw(self, win: g.GraphWin):
        self.circle.draw(win)

    def update_position(self):
        if (self.x >= 1 - self.radius) or (self.x <= -1 + self.radius):
            self.dx = -self.dx
        if (self.y >= 1 - self.radius) or (self.y <= -1 + self.radius):
            self.dy = -self.dy
        self.x += self.dx
        self.y += self.dy
        self.circle.move(self.dx, self.dy)


width = 400
height = 400

ball = Ball(0.25, -0.5, 0.1, 0.01, 0.03)

# Create a graphics window
win = g.GraphWin("Bouncing Ball", width, height)
win.setBackground("white")
win.setCoords(-1, -1, 1, 1)

# Draw the ball
ball.draw(win)

# Move the ball
while win.checkMouse() is None:
    ball.update_position()

# Close the window
win.close()
