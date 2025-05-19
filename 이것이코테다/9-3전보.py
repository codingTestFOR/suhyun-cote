"""

어떤 나라에 여러 개의 도시가 있고, 그 도시에 전보(=메시지)를 보내는 상황.
이 전보는 직접 연결된 도시를 통해서만 전달할 수 있음.
그리고 한 번의 전송에는 1단위 시간이 걸림


아이디어
1. 도시 개수 N, 통로 개수 M, 시작 도시 C 입력받기
2. 각 도시 간 연결 정보 저장하기
3.다익스트라 알고리즘으로 시작 도시 C에서 다른 도시들까지의 최단 시간 계산
4. 도달할 수 있는 도시 수 + 가장 오래 걸린 시간 출력하기

ex) 도시가 4개 있고, 전보 보낼 수 있는 경로
1번 → 2번 (시간 4)
1번 → 3번 (시간 2)
3번 → 4번 (시간 1)

 1번 도시에서 전보를 보내면?
2번 도시는 4초 걸림
3번 도시는 2초 걸림
4번 도시는 2(1→3) + 1(3→4) = 3초 걸림

"""
import sys

input = sys.stdin.readline
INF = int(1e9)

# 입력
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 그래프 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 최단 거리 갱신 함수
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 시작
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for node, cost in graph[start]:
        distance[node] = cost

    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for node, cost in graph[now]:
            new_cost = distance[now] + cost
            if new_cost < distance[node]:
                distance[node] = new_cost

dijkstra(start)

# 결과 출력
count = 0
max_dist = 0
for d in distance:
    if d != INF and d != 0:
        count += 1
        max_dist = max(max_dist, d)

print(count, max_dist)
