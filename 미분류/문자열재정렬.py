# 문자열에서 문자와 숫자를 분리하여 정렬한 후, 숫자의 합을 뒤에 붙이는 프로그램

def reorder_string(s: str) -> str:
    # 알파벳만 추출 후 정렬
    letters = sorted(c for c in s if c.isalpha())
    
    # 숫자만 추출 후 합산
    total = sum(int(c) for c in s if c.isdigit())
    
    # 알파벳과 숫자의 합을 결합하여 반환
    return "".join(letters) + (str(total) if total else "")

# 입력
s = input().strip()
print(reorder_string(s))














"""
1. c.isalpha()
isalpha()는 문자열 메서드 중 하나로, 해당 문자가 알파벳인지 아닌지를 판별합니다.

구문: c.isalpha()

동작: c가 알파벳(영문 대소문자)일 경우 True를 반환하고, 그 외에는 False를 반환합니다.

2. "".join(letters)
"".join()은 리스트 또는 **반복 가능한 객체(Iterable)**에 포함된 요소들을 하나의 문자열로 결합하는 메서드입니다.

구문: "separator".join(iterable)

separator는 결합할 때 각 요소 사이에 삽입할 구분자입니다. 이 구분자가 ""(빈 문자열)일 경우, 요소들 사이에 아무것도 넣지 않고 바로 결합합니다.

iterable은 문자열, 리스트 등 반복 가능한 객체입니다.
"""



---
# 문자열에서 문자와 숫자를 분리하여 정렬한 후, 숫자의 합을 뒤에 붙이는 프로그램

def reorder_string(s: str) -> str:
    from itertools import groupby
    
    letters, numbers = "".join(sorted(s)), 0
    for k, g in groupby(letters, key=str.isdigit):
        if k:
            numbers = sum(map(int, g))
            letters = letters.replace("".join(g), "")
            break
    
    return letters + (str(numbers) if numbers else "")

# 입력
s = input().strip()
print(reorder_string(s))
