/*다음달에 누가 가장 많은 선물을 받을까? */

def solution(friends, gifts):
    from collections import defaultdict

    n = len(friends) /*  n=친구 수 */
    idx_map = {name: i for i, name in enumerate(friends)}   /* 딕셔너리 친구이름을 숫자로 바꿔주는 딕셔너리 0,1,2*/

    # 1. 선물 기록 저장 (이중 리스트)
    gift_count = [[0] * n for _ in range(n)]  /* 선물 표를 만들어서, 다른 친구한테 준 선물 갯수 기록 (0부터 시작)*/
    
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx, receiver_idx = idx_map[giver], idx_map[receiver]
        gift_count[giver_idx][receiver_idx] += 1

    # 2. 선물 지수
    gift_index = [0] * n   /* 내가 선물 준 개수 - 내가 받은 선물개수 */
    for i in range(n):
        given = sum(gift_count[i])
        received = sum(gift_count[j][i] for j in range(n))
        gift_index[i] = given - received

    
    receive_count = [0] * n  /* 다음달 선물 받을 개수는  선물지수가 높은 사람이 추가선물받음.   */

    for i in range(n):  /* 가장큰 숫자 찾기.  */
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
    return max(receive_count) /*다음달에 가장많이 받을 선물 개수 반환*/


        -----------------------------------------------

def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    p = [0] * l
    answer = [0] * l
    gr = [[0] * l for i in range(l)]
    for i in gifts:
        a, b = i.split()
        gr[f[a]][f[b]] += 1
    for i in range(l):
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])

    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    return max(answer)

