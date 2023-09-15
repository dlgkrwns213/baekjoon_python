# https://www.acmicpc.net/problem/17387
def ccw(xa, ya, xb, yb, xc, yc):
    return (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

s = ccw(x1, y1, x2, y2, x3, y3)
t = ccw(x1, y1, x2, y2, x4, y4)
u = ccw(x3, y3, x4, y4, x1, y1)
v = ccw(x3, y3, x4, y4, x2, y2)

if s and t and u and v:  # 임의의 3점이 한 직선위에 없는 경우
    print(1 if s*t < 0 and u*v < 0 else 0)
else:
    if s == 0 and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
        print(1)
    elif t == 0 and min(x1, x2) <= x4 <= max(x1, x2) and min(y1, y2) <= y4 <= max(y1, y2):
        print(1)
    elif u == 0 and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4):
        print(1)
    elif v == 0 and min(x3, x4) <= x2 <= max(x3, x4) and min(y3, y4) <= y2 <= max(y3, y4):
        print(1)
    else:
        print(0)