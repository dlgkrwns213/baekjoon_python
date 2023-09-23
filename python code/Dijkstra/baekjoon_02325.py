# https://www.acmicpc.net/problem/2325
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


# 가장 짧은 경로 구하기
def dijkstra(start, destination):
    hq = []
    distances = [INF] * (n+1)

    heappush(hq, (0, start))
    distances[start] = 0

    log = [-1] * (n+1)

    while hq:
        now_dist, now = heappop(hq)
        if now == destination:
            break
        if distances[now] < now_dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = now_dist + nd
            if distances[nxt] > nxt_dist:
                log[nxt] = now
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    route = []
    now = destination
    while now != start:
        route.append((log[now], now))
        now = log[now]

    return route


# 경로 하나를 뺀 가장 짧은 경로
def minus_dijkstra(start, destination, x, y):
    hq = []
    distances = [INF] * (n+1)

    heappush(hq, (0, start))
    distances[start] = 0

    while hq:
        now_dist, now = heappop(hq)
        if now == destination:
            return now_dist
        if distances[now] < now_dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = now_dist + nd
            if distances[nxt] > nxt_dist:
                if (now, nxt) in ((x, y), (y, x)):
                    continue
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

shortest = dijkstra(1, n)
second = max(minus_dijkstra(1, n, a, b) for a, b in shortest)  # route 중에서 하나하나 빼면서 최소치 계산

print(second)