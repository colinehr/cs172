import graphics as g


class Ball:
    """A ball with an initial position and speed."""
    x: float
    y: float
    radius: float
    dx: float
    dy: float
    circle: g.Circle

    def __init__(self, x_start: float, y_start: float, radius: float, dx: float, dy: float):
        # set the initial state of the ball
        self.x = x_start
        self.y = y_start
        self.radius = radius
        self.dx = dx
        self.dy = dy
        # also create the graphics object which will represent the ball on the screen
        # notice that this was not an argument to __init__!
        self.circle = g.Circle(g.Point(self.x, self.y), self.radius)

    def draw(self, win: g.GraphWin):
        """Draw the ball to the window."""
        self.circle.draw(win)

    def update_position(self):
        """Animate the ball a single frame."""
        if (self.x >= 1 - self.radius) or (self.x <= -1 + self.radius):
            self.dx = -self.dx
        if (self.y >= 1 - self.radius) or (self.y <= -1 + self.radius):
            self.dy = -self.dy
        # Now we're keeping track of x and y in the Ball object, so we have to update them here
        self.x += self.dx
        self.y += self.dy
        self.circle.move(self.dx, self.dy)


# Define the width and height of our window (in pixels)
width = 400
height = 400

# Create a graphics window
win = g.GraphWin("Bouncing Ball", width, height)
win.setBackground("white")
win.setCoords(-1, -1, 1, 1)

# Create and draw the ball
ball = Ball(0.25, -0.5, 0.1, 0.01, 0.03)
ball.draw(win)

# Move the ball until the user clicks
while win.checkMouse() is None:
    ball.update_position()

# Close the window
win.close()