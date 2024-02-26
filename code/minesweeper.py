import graphics as g


win = g.GraphWin("Minesweeper", 800, 800)

# Draw an 8x8 grid in our window (you do this)
line = g.Line(g.Point(0, 100), g.Point(800, 100))
line.draw(win)
win.close()

# Initialize the minefield (a two-dimensional list) (you do this)
# Randomly place 10 "*" in the minefield 2D list
minefield = []
i = 0
while i < 8:
    minefield.append([""] * 8)

print(minefield)
