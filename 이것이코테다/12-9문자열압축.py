"""
"문자열 압축" 문제는 주어진 문자열을 연속된 동일한 문자의 개수를 활용하여 압축하는 것.

 "aabbaccc" → "2a2ba3c" 또는 "abcabcabcabcdededededede" → "2(abc)4(de)"처럼 표현할 수 있음.
"""

def compress_string(s: str) -> int:
    n = len(s)
    min_length = n
    
    for step in range(1, n // 2 + 1):  # 1부터 n//2까지 단위 설정
        compressed = ''
        prev = s[:step]
        count = 1
        
        for i in range(step, n, step):
            if s[i:i+step] == prev:  # 앞부분과 같으면 카운트 증가
                count += 1
            else:  # 다르면 그동안의 개수와 문자열 추가
                compressed += (str(count) + prev) if count > 1 else prev
                prev = s[i:i+step]
                count = 1
        
        compressed += (str(count) + prev) if count > 1 else prev
        min_length = min(min_length, len(compressed))  # 최솟값 저장
        
    return min_length

# 입력
s = input().strip()
print(compress_string(s))
