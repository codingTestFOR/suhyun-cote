/*다음달에 누가 가장 많은 선물을 받을까? */

def solution(friends, gifts):
    from collections import defaultdict

    n = len(friends)
    idx_map = {name: i for i, name in enumerate(friends)}

    # 1. 선물 기록 저장 (이중 리스트)
    gift_count = [[0] * n for _ in range(n)]
    
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx, receiver_idx = idx_map[giver], idx_map[receiver]
        gift_count[giver_idx][receiver_idx] += 1

    # 2. 선물 지수 계산
    gift_index = [0] * n  # 준 개수 - 받은 개수
    for i in range(n):
        given = sum(gift_count[i])
        received = sum(gift_count[j][i] for j in range(n))
        gift_index[i] = given - received

    # 3. 다음 달 선물 주고받기
    receive_count = [0] * n  # 다음 달 받을 선물 개수

    for i in range(n):
        for j in range(i + 1, n):
            if gift_count[i][j] > gift_count[j][i]:
                receive_count[i] += 1
            elif gift_count[i][j] < gift_count[j][i]:
                receive_count[j] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    receive_count[i] += 1
                elif gift_index[i] < gift_index[j]:
                    receive_count[j] += 1

    # 4. 가장 많이 받는 사람 찾기
    return max(receive_count)
