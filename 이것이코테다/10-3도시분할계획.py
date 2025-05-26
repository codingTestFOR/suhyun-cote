"""
마을에는 집들이 있고, 각 집은 길로 연결되어 있음.

모든 집을 연결하되, 두 개의 마을로 분리하려고 함.

즉, 최소 비용으로 모든 집을 연결하고 가장 비싼 길 하나를 끊어서 두 마을로 나누는 것.

핵심 아이디어:
최소 신장 트리 (MST)를 만든 후,
MST에서 가장 비용이 큰 간선 하나를 제거하면 두 개의 집합(=마을)로 분할됨.

사용 알고리즘:
크루스칼 알고리즘 (간선을 기준으로 정렬하고, Union-Find로 연결)

"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0
max_edge = 0

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_edge = cost

print(result - max_edge)  # 가장 비싼 간선 제거
