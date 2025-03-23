"""
캐릭터는 현재 방향 기준 왼쪽부터 탐색한다.
왼쪽에 미방문 육지가 있으면 이동하고, 회전 횟수 초기화.
네 방향 모두 이동 불가면 뒤로 후진.
뒤가 바다면 종료.

"""


n, m = map(int, input().split())
x, y, d = map(int, input().split())

map_data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
count, turn = 1, 0

while True:
    d = (d - 1) % 4
    nx, ny = x + dx[d], y + dy[d]

    if not visited[nx][ny] and not map_data[nx][ny]:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn = 0
        continue
    turn += 1

    if turn == 4:
        nx, ny = x - dx[d], y - dy[d]
        if not map_data[nx][ny]:
            x, y = nx, ny
            turn = 0
        else:
            break

print(count)
