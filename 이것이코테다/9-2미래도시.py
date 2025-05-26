"""
5 7         # 회사 수 N = 5, 경로 수 M = 7
1 2         # 연결된 회사 쌍
1 3
1 4
2 4
3 4
3 5
4 5
4 5         # 도착지점 X = 4, 거쳐야 할 회사 K = 5
"""
INF = int(1e9)

# 입력
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 k와 최종 목적지 x
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k_node in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k_node] + graph[k_node][b]_]()_]()
