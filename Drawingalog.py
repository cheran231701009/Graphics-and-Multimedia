import matplotlib.pyplot as plt

def plot(x, y): plt.plot(x, y, 'bo')

def line(x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx, sy = (1, -1)[x2 < x1], (1, -1)[y2 < y1]
    err = dx - dy
    while True:
        plot(x1, y1)
        if x1 == x2 and y1 == y2: break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x1 += sx
        if e2 < dx: err += dx; y1 += sy

def circle(cx, cy, r):
    x, y, p = 0, r, 1 - r
    while x <= y:
        for a, b in [(x, y), (y, x), (-x, y), (-y, x), (-x, -y), (-y, -x), (x, -y), (y, -x)]:
            plot(cx + a, cy + b)
        x += 1
        if p < 0: p += 2 * x + 1
        else: y -= 1; p += 2 * (x - y) + 1

def ellipse(rx, ry, cx, cy):
    x, y = 0, ry
    rx2, ry2 = rx**2, ry**2
    p1 = ry2 - rx2 * ry + 0.25 * rx2
    dx, dy = 2 * ry2 * x, 2 * rx2 * y
    while dx < dy:
        for a, b in [(x, y), (-x, y), (x, -y), (-x, -y)]: plot(cx + a, cy + b)
        x += 1; dx = 2 * ry2 * x
        if p1 < 0: p1 += dx + ry2
        else: y -= 1; dy = 2 * rx2 * y; p1 += dx - dy + ry2
    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
    while y >= 0:
        for a, b in [(x, y), (-x, y), (x, -y), (-x, -y)]: plot(cx + a, cy + b)
        y -= 1; dy = 2 * rx2 * y
        if p2 > 0: p2 -= dy + rx2
        else: x += 1; dx = 2 * ry2 * x; p2 += dx - dy + rx2

plt.figure(figsize=(6, 6))
line(10, 10, 100, 50)
circle(100, 100, 40)
ellipse(60, 30, 200, 200)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()
