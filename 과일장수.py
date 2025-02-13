def solution(k, m, score):
    result = 0  # 결과값 초기화
    score.sort(reverse=True)  # 정수를 내림차순으로 정렬
    
    for i in range(len(score) // m):
        box = score[m * i:m * (i + 1)]  # m개의 사과를 한 상자로 묶음
        result += box[-1] * m  # 가장 낮은 점수 * m (최소 점수 기준)
    
    return result
