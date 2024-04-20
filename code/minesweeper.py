import graphics as g
import random


def init_minefield() -> list[list[str]]:
    # Create the minefield variable
    minefield = []
    i = 0
    while i < 8:
        row = [""] * 8
        minefield.append(row)
        i += 1
    # Add mines randomly, making sure to not duplicate
    count = 0
    while count < 10:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if minefield[y][x] != "*":
            minefield[y][x] = "*"
            count += 1
    # Added data about neighboring mines to each square that isn't a mine
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            if minefield[i][j] != "*":
                minefield[i][j] = str(neighbor_mines(minefield, i, j))
            j += 1
        i += 1
    return minefield


def neighbor_mines(minefield, row, col) -> int:
    # you write this
    return 0


def init_window() -> g.GraphWin:
    win = g.GraphWin("Minesweeper", 400, 400)
    win.setBackground("white")
    win.setCoords(0, 0, 8, 8)

    # draw our grid
    i = 1
    while i < 8:
        line = g.Line(g.Point(0, i), g.Point(8, i))
        line.draw(win)
        line = g.Line(g.Point(i, 0), g.Point(i, 8))
        line.draw(win)
        i += 1
    return win


def draw_square(minefield, row: int, col: int):
    if minefield[row][col] == "*":
        circle = g.Circle(g.Point(col + 0.5, row + 0.5), 0.25)
        circle.setFill("black")
        circle.draw(win)
    else:
        text = g.Text(g.Point(col + 0.5, row + 0.5), minefield[row][col])
        text.draw(win)


def reveal():
    # reveals the part of the board from a user click (you write this)
    pass


# main code starts here
minefield = init_minefield()
win = init_window()

# wait for the user to click the mouse and then reveal the spot that they click
while True:
    click = win.getMouse()
    x = int(click.getX())
    y = int(click.getY())
    print(minefield[y][x])
    draw_square(minefield, y, x)


win.close()
