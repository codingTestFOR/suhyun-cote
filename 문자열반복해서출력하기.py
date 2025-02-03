"""
문자열 str과 정수 n이 주어집니다.
str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

"""
"""
입력 string 5
출력 stringstringstringstringstring
"""

str, n = input().strip().split(' ')
n = int(n)
print(str * n)

