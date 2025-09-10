import matplotlib.pyplot as plt
import numpy as np
from collections import deque
w,h=300,300
c=np.ones((h,w,3),dtype=np.uint8)*255
def poly(v):
    for i in range(len(v)):
        x1,y1=v[i]
        x2,y2=v[(i+1)%len(v)]
        line(x1,y1,x2,y2)
def line(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    x,y=x1,y1
    sx=1 if x2>x1 else -1
    sy=1 if y2>y1 else -1
    if dx>dy:
        e=dx/2
        while x!=x2:
            c[y,x]=[0,0,0]
            e-=dy
            if e<0:
                y+=sy
                e+=dx
            x+=sx
        c[y,x]=[0,0,0]
    else:
        e=dy/2
        while y!=y2:
            c[y,x]=[0,0,0]
            e-=dx
            if e<0:
                x+=sx
                e+=dy
            y+=sy
        c[y,x]=[0,0,0]
def fill(sx,sy,t,f):
    t=np.array(t,dtype=np.uint8)
    f=np.array(f,dtype=np.uint8)
    if sx<0 or sx>=w or sy<0 or sy>=h:return
    if not np.array_equal(c[sy,sx],t):return
    q=deque([(sx,sy)])
    while q:
        x,y=q.popleft()
        if x<0 or x>=w or y<0 or y>=h:continue
        if np.array_equal(c[y,x],t):
            c[y,x]=f
            q.append((x+1,y))
            q.append((x-1,y))
            q.append((x,y+1))
            q.append((x,y-1))
v=[(50,50),(250,50),(200,200),(100,250),(50,150)]
poly(v)
fill(150,100,[255,255,255],[255,0,0])
plt.imshow(c)
plt.axis('off')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
w,h=300,300
c=np.ones((h,w,3),dtype=np.uint8)*255
def poly(v):
    for i in range(len(v)):
        x1,y1=v[i]
        x2,y2=v[(i+1)%len(v)]
        line(x1,y1,x2,y2)
def line(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    x,y=x1,y1
    sx=1 if x2>x1 else -1
    sy=1 if y2>y1 else -1
    if dx>dy:
        e=dx/2
        while x!=x2:
            c[y,x]=[0,0,0]
            e-=dy
            if e<0:
                y+=sy
                e+=dx
            x+=sx
        c[y,x]=[0,0,0]
    else:
        e=dy/2
        while y!=y2:
            c[y,x]=[0,0,0]
            e-=dx
            if e<0:
                x+=sx
                e+=dy
            y+=sy
        c[y,x]=[0,0,0]
def fill(sx,sy,t,f):
    t=np.array(t,dtype=np.uint8)
    f=np.array(f,dtype=np.uint8)
    if sx<0 or sx>=w or sy<0 or sy>=h:return
    if not np.array_equal(c[sy,sx],t):return
    q=deque([(sx,sy)])
    while q:
        x,y=q.popleft()
        if x<0 or x>=w or y<0 or y>=h:continue
        if np.array_equal(c[y,x],t):
            c[y,x]=f
            q.append((x+1,y))
            q.append((x-1,y))
            q.append((x,y+1))
            q.append((x,y-1))
v=[(50,50),(250,50),(200,200),(100,250),(50,150)]
poly(v)
fill(150,100,[255,255,255],[255,0,0])
plt.imshow(c)
plt.axis('off')
plt.show()
