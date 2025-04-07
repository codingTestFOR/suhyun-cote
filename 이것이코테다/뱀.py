"""
n x n 보드 위에 뱀이 움직인다.
뱀은 1초마다 머리를 한 칸 이동한다.
사과를 만나면 몸이 길어짐 (꼬리 안 줄임).
사과가 없으면 머리 한 칸 늘고 꼬리는 줄어서 길이 유지.
자기 몸에 부딪히거나, 벽에 부딪히면 게임 끝.
정해진 시간에 왼쪽(L), 오른쪽(D) 으로 방향을 바꾼다.
"""
n = int(input())  # 보드 크기
board = [[0] * n for _ in range(n)]

k = int(input())  # 사과 개수
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1  # 사과는 1로 표시

l = int(input())  # 방향 전환 횟수
directions = {}
for _ in range(l):
    t, c = input().split()
    directions[int(t)] = c

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

# 뱀의 시작 상태
snake = [(0, 0)]
x, y = 0, 0
direction = 0
time = 0

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    # 벽에 부딪힘
    if not (0 <= x < n and 0 <= y < n):
        break
    # 자기 몸에 부딪힘
    if (x, y) in snake:
        break

    snake.append((x, y))  # 머리 추가

    if board[x][y] == 1:
        board[x][y] = 0  # 사과 먹으면 꼬리 그대로 (길어짐)
    else:
        snake = snake[1:]  # 사과 없으면 꼬리 제거 (길이 유지)

    # 방향 전환
    if time in directions:
        direction = turn(direction, directions[time])

print(time)
