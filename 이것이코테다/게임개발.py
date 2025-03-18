# 변수 : N M 맵의 세로 가로 크기
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 변수 : d 방문 위치 표시맵
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]    # 리스트 컴프리헨션 문법으로 2차원 리스트 초기화

# 변수 : x y 현재 좌표, direction 바라보는 방향 (0 북 1 동 2 남 3 서)
# 현재 캐릭터의 X, Y 좌표, 방향을 입력받기
x, y, dirextion = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 변수 : N개 줄의 0, 1
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction     # direction 변수가 함수 바깥에서 선언된 전역변수
    direction -= 1       # 왼쪽으로 회전
    if direction == -1:  # 북쪽에서 회전하면 서쪽 : -1 → 3
        direction = 3

# 시뮬레이션 시작
count = 1    # 첫
trun_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx(direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:    # d 방문위치, array 바다위치
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1    # 한번 더 회전
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:    # 3의 경우 : 바라보는 방향 유지, 한 칸 뒤로
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break    # 빠져나감
        turn_time = 0     # 다시 1의 경우로 돌아감
    
# 정답 출력
print(count)
