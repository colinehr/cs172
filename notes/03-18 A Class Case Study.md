# Refactoring with Classes: A Case Study

Here I show an example of refactoring already working code to make use of classes. The code will be the *bouncing ball* code we created earlier in class.

## Version 1: No Classes

```python
import graphics as g

# Define the width and height of our window (in pixels)
width = 400
height = 400

# Define the starting position of the ball as well as its radius
x_start = 0.25
y_start = -0.5
radius = 0.1

# Define the starting speed (dx/dy = change of x/y in pixels each time interval)
dx = 0.01
dy = 0.03

# Create a graphics window
win = g.GraphWin("Bouncing Ball", width, height)
win.setBackground("white")
win.setCoords(-1, -1, 1, 1)

# Create a circle
ball = g.Circle(g.Point(x_start, y_start), radius)
ball.setFill("black")
ball.draw(win)

# Move the ball
while win.checkMouse() is None:
    # The ball object keeps track of its current x and y
    x = ball.getCenter().getX()
    y = ball.getCenter().getY()
    # Bounce the ball if it would go out of bounds
     if (x >= 1 - radius) or (x <= -1 + radius):
        dx = -dx
     if (y >= 1 - radius) or (y <= -1 + radius):
        dy = -dy
    # Move the ball on the screen; this updates the x and y coords of ball
    ball.move(dx, dy)

# Close the window
win.close()
```

## Version 2: The `ball` Class

```python
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
```

## Version 3: A Slight Simplification

```python
import graphics as g

class Ball:
    """A ball with an initial position and speed."""
    circle: g.Circle
    dx: float
    dy: float

    def __init__(self, x_start: float, y_start: float, radius: float, dx: float, dy: float):
        # Set the initial state of the ball
        # Note: the circle object will keep track of its x and y, so we don't have to
        self.circle = g.Circle(g.Point(self.x, self.y), self.radius)
        # Set the initial speed
        self.dx = dx
        self.dy = dy

    def draw(self, win: g.GraphWin):
        """Draw the ball to the window."""
        self.circle.draw(win)

    def update_position(self):
        """Animate the ball a single frame."""
        # The ball object keeps track of its current x and y and its radius
        x = self.circle.getCenter().getX()
        y = self.circle.getCenter().getY()
        radius = self.circle.getRadius()
        if (x >= 1 - radius) or (x <= -1 + radius):
            self.dx = -self.dx
        if (y >= 1 - radius) or (y <= -1 + radius):
            self.dy = -self.dy
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
```

## Version 4: Hiding the Internal Variables and using Setters

```python
import graphics as g

class Ball:
    """A ball with an initial position and speed."""
    _circle: g.Circle
    _dx: float
    _dy: float

    def __init__(self, x_start: float, y_start: float, radius: float, dx: float, dy: float):
        # Set the initial state of the ball
        # Note: the circle object will keep track of its x and y, so we don't have to
        self._circle = g.Circle(g.Point(self.x, self.y), self.radius)
        # Set the initial speed
        self._dx = dx
        self._dy = dy

    @property
    def x(self):
        return self._circle.getX()

    @property
    def y(self):
        return self._circle.getY()

    @property
    def radius(self):
        return self._circle.getRadius()

    @property
    def dx(self):
        return self._dx()

    @property
    def dy(self):
        return self._dy()

    def draw(self, win: g.GraphWin):
        """Draw the ball to the window."""
        self.circle.draw(win)

    def update_position(self):
        """Animate the ball a single frame."""
        if (self.x >= 1 - self.radius) or (self.x <= -1 + self.radius):
            self.dx = -self.dx
        if (self.y >= 1 - self.radius) or (self.y <= -1 + self.radius):
            self.dy = -self.dy
        self._circle.move(self.dx, self.dy)

    def __str__(self) -> str:
        return "Ball at (" + self.x + ", " + self.y ")"


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
```