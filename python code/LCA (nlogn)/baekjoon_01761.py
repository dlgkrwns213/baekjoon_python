# https://www.acmicpc.net/problem/1761
import sys
from math import ceil, log2
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def set_parent(now, dep, dist):
    depth[now] = dep
    distances[now] = dist
    for nxt, nxt_dist in graph[now]:
        if depth[nxt] != -1:
            continue

        ancestor[nxt][0] = now
        set_parent(nxt, dep+1, dist+nxt_dist)


def set_ancestor():
    set_parent(1, 0, 0)  # 임의의 노드 중 루트르 1로 설정 (다른 노드로 해도 상관 없음)

    for i in range(1, size):
        for j in range(1, n+1):
            ancestor[j][i] = ancestor[ancestor[j][i-1]][i-1]


def lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    for i in range(size-1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            y = ancestor[y][i]

    if x == y:
        return x

    for i in range(size-1, -1, -1):
        if ancestor[x][i] != ancestor[y][i]:
            x = ancestor[x][i]
            y = ancestor[y][i]

    return ancestor[x][0]


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

# 각 노드들의 조상 설정 (root: 1로 가정한다)
size = ceil(log2(n))
ancestor, depth = [[0]*size for _ in range(n+1)], [-1] * (n+1)
distances = [0] * (n+1)  # root 부터 해당 node까지의 거리
set_ancestor()

m = int(input())
ans = [0] * m
for idx in range(m):
    a, b = map(int, input().split())
    # node x가 node y의 조상일 떄 node x에서 node y의 거리: distance[x] - distance[y]
    ans[idx] = distances[a] + distances[b] - 2 * distances[lca(a, b)]

print('\n'.join(map(str, ans)))