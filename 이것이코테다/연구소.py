
# 입력
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_safe = 0  # 결과 저장

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

# 벽 세우기 (백트래킹 방식)
def make_wall(cnt):
    global max_safe
    if cnt == 3:
        temp = copy.deepcopy(lab)
        spread_virus(temp)
        max_safe = max(max_safe, count_safe(temp))
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(cnt + 1)
                lab[i][j] = 0

make_wall(0)
print(max_safe)
