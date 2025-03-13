

"""
주어진 arr의 행(row)과 열(column)의 개수를 맞추기 위해 0을 추가하는 문제입니다.
즉,

행(row)의 개수가 더 많다면 → 모든 행에 0을 추가해서 열(column)의 개수를 맞춤
열(column)의 개수가 더 많다면 → 새로운 행을 추가해서 행(row)의 개수를 맞춤
 해결 방법
주어진 2차원 배열 arr의 행(row) 개수와 열(column) 개수를 구함
행(row)과 열(column)의 개수 중 더 큰 값을 size로 설정
새로운 size × size 크기의 배열을 만들고, 기존 배열 값을 복사
빈 자리(추가된 부분)는 0으로 채움

row = len(arr), col = len(arr[0]) → 행(row)과 열(column)의 개수를 구함
size = max(row, col) → 정사각형 배열을 만들기 위한 최대 크기 설정
new_arr = [[0] * size for _ in range(size)] → 0으로 채워진 size × size 배열 생성
기존 배열의 값 복사
for i in range(row): for j in range(col): → 기존 arr의 값들을 new_arr에 옮김
변환된 새로운 2차원 배열을 반환

"""
def solution(arr):
    n=len(arr)
    m=len(arr[0])
    if n>m:
        for i in range(n):
            for j in range(n-m):
                arr[i].append(0)
    else:
        for i in range(m-n):
            arr.append([0]*m)

    return arr
