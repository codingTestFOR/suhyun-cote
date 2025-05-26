"""
문제 개요:
여러 과목이 있고, 선수 과목(먼저 들어야 하는 과목)이 있음.

각 과목마다 강의 시간이 주어짐.

모든 과목에 대해 최소 이수 시간을 계산해야 함.

핵심 아이디어:
과목 간 선후관계 = 방향 그래프

먼저 들어야 하는 과목이 있다면, 해당 과목이 끝난 후 다음 과목을 시작할 수 있음.
위상 정렬을 사용하여 순서대로 계산 + 각 과목까지 걸리는 최장 시간을 누적 (DP 사용)

사용 알고리즘:
위상 정렬 + DP


"""

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 강의 시간
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

result = time[:]  # 각 과목까지의 누적 시간
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        result[i] = max(result[i], result[now] + time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n + 1):
    print(result[i])
