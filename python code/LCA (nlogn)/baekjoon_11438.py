# https://www.acmicpc.net/problem/11438
import sys
from math import ceil, log2
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


# dfs
def set_parent(now, dep):
    depth[now] = dep
    for nxt in graph[now]:
        if depth[nxt] != -1:
            continue

        ancestors[nxt][0] = now
        set_parent(nxt, dep+1)


def set_ancestor():
    set_parent(1, 0)  # root: 1, graph: tree

    for i in range(1, size):
        for j in range(1, n+1):
            '''
            ancestors[j][i-1]을 k라고 할때,
            k: j의 (2 ** (n-1))번쨰 조상
            ancestors[k][i-1]: k의 (2 ** (n-1))번쨰 조상

            -> ancestors[k][i-1]은 j의 (2 ** (n-1) + 2 ** (n-1))번째 조상
            -> ancestors[j][i] = ancestors[k][i-1] = ancestors[ancestors[j][i-1]][i-1]
            '''
            ancestors[j][i] = ancestors[ancestors[j][i-1]][i-1]


def lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    # 두 노드의 깊이를 맞춰줌
    for i in range(size-1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            y = ancestors[y][i]

    if x == y:
        return x

    # x와 y의 parent가 같을 때 까지 실행
    # lca의 값이 z일때 z가 가장 가까운 조상이라는 보장이 없으므로 z의 자식을 구한 후 부모인 z를 구해주어야 한다.
    for i in range(size-1, -1, -1):
        if ancestors[x][i] != ancestors[y][i]:
            x = ancestors[x][i]
            y = ancestors[y][i]

    return ancestors[x][0]


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

size = ceil(log2(n))
# ancestors[person][gen]: person의 2 ** gen번쨰 조상
ancestors, depth = [[0]*size for _ in range(n+1)], [-1] * (n+1)
set_ancestor()

m = int(input())
ans = [0] * m
for idx in range(m):
    a, b = map(int, input().split())
    ans[idx] = lca(a, b)

print('\n'.join(map(str, ans)))