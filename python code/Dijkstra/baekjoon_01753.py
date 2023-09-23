# https://www.acmicpc.net/problem/1753
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    hq = []

    heappush(hq, (0, start))
    distances[start] = 0

    while hq:
        now_weight, now = heappop(hq)

        for nxt, nw in graph[now]:
            nxt_weight = now_weight + nw
            if distances[nxt] > nxt_weight:
                distances[nxt] = nxt_weight
                heappush(hq, (nxt_weight, nxt))


n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distances = [INF] * (n+1)
dijkstra(k)

print('\n'.join(map(lambda dist: str(dist) if dist != INF else 'INF', distances[1:])))