# https://www.acmicpc.net/problem/17386
def ccw(xa, ya, xb, yb, xc, yc):
    return (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

s = ccw(x1, y1, x2, y2, x3, y3)
t = ccw(x1, y1, x2, y2, x4, y4)
u = ccw(x3, y3, x4, y4, x1, y1)
v = ccw(x3, y3, x4, y4, x2, y2)

print(1 if s*t < 0 and u*v < 0 else 0)