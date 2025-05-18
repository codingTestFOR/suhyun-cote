import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 입력 받기
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # x에서 y로 가는 비용이 z

# 최단 거리 테이블
distance = [INF] * (n + 1)

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, cost in graph[now]:
            new_dist = dist + cost
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

dijkstra(start)

# 결과 처리
count = 0
max_dist = 0
for d in distance:
    if d != INF and d != 0:
        count += 1
        max_dist = max(max_dist, d)

print(count, max_dist)
