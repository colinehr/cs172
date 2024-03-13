import graphics as g


with open("code/para1.txt") as f:
    text = f.read()
letters = "abcdefghijklmnopqrstuvwxyz"
counts = [0] * 26
for ch in text:
    if ch.lower() in letters:
        counts[letters.find(ch.lower())] += 1

win = g.GraphWin("Letter Distribution", 400, 400)
win.setCoords(-5, -0.1, 27, 1.1)
g.Line(g.Point(0, 0), g.Point(26, 0)).draw(win)
for i, letter in enumerate(letters):
    g.Text(g.Point(i + 0.5, -0.05), letter).draw(win)
    if counts[i] != 0:
        bar = g.Rectangle(g.Point(i, 0), g.Point(i + 0.9, counts[i]/max(counts)))
        bar.setFill("red")
        bar.draw(win)
g.Line(g.Point(0, 0), g.Point(0, 1)).draw(win)
g.Text(g.Point(-1, 0), "0").draw(win)
g.Text(g.Point(-1, 1), max(counts)).draw(win)


win.getMouse()
win.close()
