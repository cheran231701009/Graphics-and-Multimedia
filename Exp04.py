import matplotlib.pyplot as plt

L, R, B, T = 0, 1, 2, 3

def inside(p, e, win):
    x, y = p
    xmin, xmax, ymin, ymax = win
    if e == L: return x >= xmin
    if e == R: return x <= xmax
    if e == B: return y >= ymin
    if e == T: return y <= ymax

def intersect(p1, p2, e, win):
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax, ymin, ymax = win
    if e == L: return (xmin, y1 + (y2 - y1) * (xmin - x1) / (x2 - x1))
    if e == R: return (xmax, y1 + (y2 - y1) * (xmax - x1) / (x2 - x1))
    if e == B: return (x1 + (x2 - x1) * (ymin - y1) / (y2 - y1), ymin)
    if e == T: return (x1 + (x2 - x1) * (ymax - y1) / (y2 - y1), ymax)

def clip_polygon(poly, win):
    out = poly
    for e in [L, R, B, T]:
        inp, out = out, []
        if not inp: break
        s = inp[-1]
        for p in inp:
            if inside(p, e, win):
                if not inside(s, e, win):
                    out.append(intersect(s, p, e, win))
                out.append(p)
            elif inside(s, e, win):
                out.append(intersect(s, p, e, win))
            s = p
    return out

def draw_polygon(pts, col, lbl):
    if not pts: return
    x, y = zip(*(pts + [pts[0]]))
    plt.plot(x, y, color=col, label=lbl)

win = (100, 300, 100, 300)
poly = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 350), (150, 300)]
clipped = clip_polygon(poly, win)

plt.figure(figsize=(8, 8))
draw_polygon(poly, 'blue', "Original")
draw_polygon([(win[0], win[2]), (win[1], win[2]), (win[1], win[3]), (win[0], win[3])], 'black', "Window")
draw_polygon(clipped, 'red', "Clipped")
plt.legend()
plt.title("Sutherland-Hodgman Polygon Clipping")
plt.grid(True)
plt.axis("equal")
plt.show()
