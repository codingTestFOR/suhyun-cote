"""
캐릭터는 현재 방향 기준 왼쪽부터 탐색한다.
왼쪽에 미방문 육지가 있으면 이동하고, 회전 횟수 초기화.
네 방향 모두 이동 불가면 뒤로 후진.
뒤가 바다면 종료.

"""

def max_sum_of_sequence(N, sequence):
    sequence.sort(reverse=True)
    result = 0
    i = 0
    
    # 2 이상인 숫자들은 묶어서 곱하고, 1과 0은 각각 더해주기
    while i < N - 1:
        if sequence[i] > 1 and sequence[i + 1] > 1:
            result += sequence[i] * sequence[i + 1]
            i += 2
        else:
            result += sequence[i]
            i += 1

    # 마지막 남은 수 처리 (1이거나 0이면 그냥 더함)
    if i < N:
        result += sequence[i]

    return result
