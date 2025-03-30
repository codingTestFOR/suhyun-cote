# 문자열에서 문자와 숫자를 분리하여 정렬한 후, 숫자의 합을 뒤에 붙이는 프로그램

def reorder_string(s: str) -> str:
    letters = sorted(c for c in s if c.isalpha())  # 알파벳만 추출 후 정렬
    total = sum(int(c) for c in s if c.isdigit())  # 숫자만 추출 후 합산
    
    return "".join(letters) + (str(total) if total else "")

# 입력
s = input().strip()
print(reorder_string(s))

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
