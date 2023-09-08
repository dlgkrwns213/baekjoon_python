# https://www.acmicpc.net/problem/13511
import sys
from math import ceil, log2
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def set_parent(now, dep, weight):
    depth[now] = dep
    weights[now] = weight
    for nxt, nxt_weight in graph[now]:
        if depth[nxt] != -1:
            continue

        ancestor[nxt][0] = now
        set_parent(nxt, dep+1, weight+nxt_weight)


def set_ancestor():
    set_parent(1, 0, 0)  # 무방향 트리이므로 root: 1로 설정 (임의의 한 노드)

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


def get_kth_ancestor(node, k):
    x = node
    for i in range(size-1, -1, -1):
        if k & 1 << i:  # bit 연산 이용
            x = ancestor[x][i]
    return x


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

size = ceil(log2(n))
ancestor, depth = [[0]*size for _ in range(n+1)], [-1] * (n+1)
weights = [0] * (n+1)  # root 에서 해당 node 까지의 비용
set_ancestor()

m = int(input())
ans = [0] * m
for idx in range(m):
    q, *nums = map(int, input().split())
    if q == 1:
        u, v = nums
        ans[idx] = weights[u] + weights[v] - 2 * weights[lca(u, v)]
    else:
        u, v, k = nums
        k -= 1  # 시작점을 포함하므로 -1
        uv_lca = lca(u, v)
        if depth[u] - depth[uv_lca] < k:  # k번째 node가 u의 조상이 아닐 경우
            k = depth[u] + depth[v] - 2 * depth[uv_lca] - k  # v의 조상이므로 k를 다시 구해줌
            ans[idx] = get_kth_ancestor(v, k)
        else:
            ans[idx] = get_kth_ancestor(u, k)

print('\n'.join(map(str, ans)))