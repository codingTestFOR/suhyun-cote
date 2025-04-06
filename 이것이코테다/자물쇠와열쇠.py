"""
"자물쇠와 열쇠" 문제는 주어진 자물쇠와 열쇠의 모양을 비교하여 열쇠를 자물쇠에 맞출 수 있는지 확인하는 문제입니다. 자물쇠를 돌리거나 위치를 바꾸어 열쇠가 맞을 때 "True"를 반환한다.
문제 해결 아이디어:
자물쇠의 크기와 열쇠의 크기를 비교해야 하며, 열쇠를 회전시켜 자물쇠에 맞출 수 있는지 확인해야 한다.
자물쇠 크기 n x n과 열쇠 크기 m x m이 주어지며, 열쇠는 여러 번 회전하면서 자물쇠에 맞을 수 있는지 확인한다.

"""

def rotate_key(key):
    return list(zip(*key[::-1]))

def check_lock(lock, key, lock_offset):
    n = len(lock)
    m = len(key)
    
    # 자물쇠 범위 내에서 열쇠를 맞춰보기
    for i in range(lock_offset[0], lock_offset[0] + m):
        for j in range(lock_offset[1], lock_offset[1] + m):
            if 0 <= i < n and 0 <= j < n:
                if lock[i][j] != key[i - lock_offset[0]][j - lock_offset[1]]:
                    return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 자물쇠 주변을 1로 둘러싼 새로운 배열 생성
    lock_expanded = [[1] * (n + 2 * m) for _ in range(n + 2 * m)]
    for i in range(n):
        for j in range(n):
            lock_expanded[m + i][m + j] = lock[i][j]
    
    # 열쇠를 회전시키면서 자물쇠에 맞추기
    for rotation in range(4):
        key_rotated = key
        for _ in range(rotation):
            key_rotated = rotate_key(key_rotated)
        
        # 열쇠를 자물쇠에 맞춰보기
        for i in range(m + 1):  # 열쇠를 자물쇠 범위 내에서 맞추기
            for j in range(m + 1):
                if check_lock(lock_expanded, key_rotated, (i, j)):
                    return True
    return False

# 예시 입력
key = [[0, 0, 1], [1, 1, 1], [0, 0, 0]]
lock = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]

print(solution(key, lock))  # True 또는 False


------
def rotate_90(matrix):
    # 90도 회전: 시계방향
    return [list(reversed(col)) for col in zip(*matrix)]

def can_unlock(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    expanded_size = lock_size + 2 * key_size

    # 자물쇠 확장 (열쇠가 바깥까지 이동할 수 있도록)
    expanded_lock = [[0] * expanded_size for _ in range(expanded_size)]

    # 확장 자물쇠의 중앙에 원래 자물쇠 배치
    for i in range(lock_size):
        for j in range(lock_size):
            expanded_lock[i + key_size][j + key_size] = lock[i][j]

    # 4번 회전
    for _ in range(4):
        key = rotate_90(key)

        # 열쇠를 이동시키며 확인
        for x in range(0, expanded_size - key_size + 1):
            for y in range(0, expanded_size - key_size + 1):

                # 열쇠 끼워보기
                for i in range(key_size):
                    for j in range(key_size):
                        expanded_lock[x + i][y + j] += key[i][j]

                # 중앙 자물쇠 부분이 전부 1인지 확인 (구멍만 맞고 겹치면 안됨)
                if is_unlocked(expanded_lock, key_size, lock_size):
                    return True

                # 다시 원상복구
                for i in range(key_size):
                    for j in range(key_size):
                        expanded_lock[x + i][y + j] -= key[i][j]

    return False

def is_unlocked(expanded, offset, size):
    for i in range(size):
        for j in range(size):
            if expanded[offset + i][offset + j] != 1:
                return False
    return True
