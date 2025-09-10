import numpy as np
import matplotlib.pyplot as plt

def draw(p, lbl, col):
    x, y = zip(*p)
    x += (x[0],)
    y += (y[0],)
    plt.plot(x, y, color=col, label=lbl)

def trans(p, tx, ty):
    T = np.array([[1,0,tx],[0,1,ty],[0,0,1]])
    return apply(p,T)

def scale(p, sx, sy):
    S = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
    return apply(p,S)

def rot(p, a):
    r = np.radians(a)
    R = np.array([[np.cos(r),-np.sin(r),0],[np.sin(r),np.cos(r),0],[0,0,1]])
    return apply(p,R)

def apply(p,m):
    res=[]
    for x,y in p:
        v = np.array([x,y,1])
        t = m @ v
        res.append((t[0],t[1]))
    return res

tri = [(0,0),(100,0),(50,80)]
t1 = trans(tri,120,50)
t2 = scale(tri,1.5,1.5)
t3 = rot(tri,45)

plt.figure(figsize=(8,8))
draw(tri,"Orig",'blue')
draw(t1,"Trans",'green')
draw(t2,"Scale",'orange')
draw(t3,"Rot",'red')
plt.title("2D Transformations")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
