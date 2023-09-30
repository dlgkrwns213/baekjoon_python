# https://www.acmicpc.net/problem/10473
import sys
from heapq import heappush, heappop
from math import sqrt
input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def dijkstra():
    hq = []
    times = [0] * (n+1)

    # 출발지로부터 다이렉트로 가는 시간 측정
    for idx, location in enumerate(locations):
        x, y = location
        time = get_distance(sx, sy, x, y) / 5
        heappush(hq, (time, idx))
        times[idx] = time

    while hq:
        now_time, now = heappop(hq)
        if now == n:
            return now_time
        if times[now] < now_time:
            continue

        for nxt in range(n+1):
            dist = distances[now][nxt]
            if dist <= 30:
                nxt_time = now_time + dist / 5
            elif dist <= 50:
                nxt_time = now_time + 12 - dist / 5  # 2 + (50 - dist) / 5
            else:
                nxt_time = now_time + dist / 5 - 8  # 2 + (dist - 50) / 5

            if times[nxt] > nxt_time:
                times[nxt] = nxt_time
                heappush(hq, (nxt_time, nxt))


sx, sy = map(float, input().split())
dx, dy = map(float, input().split())
n = int(input())
locations = [list(map(float, input().split())) for _ in range(n)] + [[dx, dy]]  # 목적지만 추가해주기

distances = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            continue
        xi, yi = locations[i]
        xj, yj = locations[j]
        distances[i][j] = get_distance(xi, yi, xj, yj)

print(dijkstra())