# https://www.acmicpc.net/problem/2233
# stack + tree
def get_graph() -> set:
    now, node = 0, 1
    rottens = set()
    for idx, v in enumerate(routes):
        if not v:
            if idx in (x, y):
                rottens.add(node)

            in_out[node].append(idx)  # 들어온 후에야 나갈수 있으므로 순서 고려 x
            stack.append(node)
            graph[now].append(node)
            parents[node] = now
            depth[node] = depth[now] + 1
            now = node  # now = stack[-1]
            node += 1
        else:
            if idx in (x, y):
                rottens.add(stack[-1])

            in_out[stack[-1]].append(idx)
            stack.pop()
            now = stack[-1]

    return rottens


# LCA
def get_common_parent(a: int, b: int) -> int:
    if depth[a] > depth[b]:
        a, b = b, a

    for _ in range(depth[b]-depth[a]):
        b = parents[b]

    while a != b:
        a = parents[a]
        b = parents[b]

    return a


n = int(input())
routes = list(map(int, input()))
x, y = map(lambda num: int(num)-1, input().split())

stack = [0]
stack, graph, in_out = [0], [[] for _ in range(n+1)], [[] for _ in range(n+1)]
parents, depth = [-1] * (n+1), [0] * (n+1)
rotten_apples = get_graph()
if len(rotten_apples) == 1:  # 썩은 사과가 1개인 경우
    i, j = in_out[rotten_apples.pop()]
    print(i+1, j+1)
else:
    x, y = rotten_apples
    common_parent = get_common_parent(x, y)
    i, j = in_out[common_parent]
    print(i+1, j+1)