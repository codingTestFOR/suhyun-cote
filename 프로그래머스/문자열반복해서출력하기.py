"""
문자열 str과 정수 n이 주어집니다.
str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

입력 string 5
출력 stringstringstringstringstring


인풋으로 사용자 입력 받은 후 , strip() 앞뒤의 공백을 제거함. 
split('') 입력받은 문자열을 공백기준으로 분리하여 리스트로 만듦
첫번째 값 문자열 a, 두번째 값 반복횟수 b

a * int(b)는 문자열 a를 b번 반복한 결과를 생성
"""

a, b = input().strip().split(' ')
print(a * int(b))
