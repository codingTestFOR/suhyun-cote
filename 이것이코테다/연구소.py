"""
바이러스 확산을 막기 위해 벽을 세움. 벽의 개수는 3개 세움

input                 output
7 7                       27
2 0 0 0 1 1 0              벽을 적절히 3개 세우고, 바이러스를 퍼뜨린 후,안전한 칸(0)이 최대로 남은 개수는 27칸
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

0빈칸, 1 벽 , 2 바이러스
"""


# 입력
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for i in range(n)]

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maximum = 0  # 결과 저장

# 바이러스 확산
def spread_virus(temp):
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                dfs_virus(temp, i, j)

def dfs_virus(temp, x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            dfs_virus(temp, nx, ny)

# 안전영역 계산
def count_safe(temp):
    return sum(row.count(0) for row in temp)

# 벽 세우기 (백트래킹)
def make_wall(cnt):
    global maximum
    if cnt == 3:
        temp = [row[:] for row in lab]  # deepcopy 대신 리스트 컴프리헨션!
        spread_virus(temp)              # 이름 일치!
        maximum = max(maximum, count_safe(temp))
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(cnt + 1)
                lab[i][j] = 0

make_wall(0)
print(maximum)
