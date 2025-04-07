"""
n x n 보드 위에 뱀이 움직인다.
뱀은 1초마다 머리를 한 칸 이동한다.
사과를 만나면 몸이 길어짐 (꼬리 안 줄임).
사과가 없으면 머리 한 칸 늘고 꼬리는 줄어서 길이 유지.
자기 몸에 부딪히거나, 벽에 부딪히면 게임 끝.
정해진 시간에 왼쪽(L), 오른쪽(D) 으로 방향을 바꾼다.
"""
n = int(input())  #보드
k = int(input())  #사과

#사과위치
board = [[0] * n for _ in range(n)]

# 사과 위치 표시 (1이면 사과 있음)
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1  # 문제에선 (1,1)부터 시작이라 -1 해줌

# 방향 전환 정보 입력
l = int(input())  # 회전 횟수
directions = {}
for _ in range(l):
    t, c = input().split()  # t: 몇 초 후, c: 방향 (L or D)
    directions[int(t)] = c

# 초기값 설정
dx = [0, 1, 0, -1]  # 동, 남, 서, 북 방향 (행 기준 이동)
dy = [1, 0, -1, 0]  # 동, 남, 서, 북 방향 (열 기준 이동)
direction = 0       # 처음엔 오른쪽(0번 방향)

time = 0  # 시간 (초 단위)
snake = deque([(0, 0)])  # 뱀의 처음 위치는 (0, 0)

x, y = 0, 0  # 현재 머리 위치

def turn(dir, c):
    if c == 'L':  # 왼쪽 회전
        return (dir-1) % 4
    else:         # 오른쪽 회전
        return (dir+1) % 4

while True:
    time += 1  # 1초 지남

    # 다음 위치 계산
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 게임 끝 조건: 벽에 부딪히거나, 자기 몸에 부딪힘
    if not (0 <= nx < n and 0 <= ny < n):
        break  # 벽 밖으로 나가면 끝
    if (nx, ny) in snake:
        break  # 자기몸 부딪히면 끝

    # 이동: 머리 추가
    snake.append((nx, ny))
    if board[nx][ny] == 1:  # 사과가 있으면
        board[nx][ny] = 0   # 사과 먹음
        
    else:
        snake.popleft()

    x, y = nx, ny  

    if time in directions: 
        direction = turn(direction, directions[time])

print(time)
