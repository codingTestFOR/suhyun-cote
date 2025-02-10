"""
- 개인정보는 각기 다른 약관에 따라 보관 기간이 정해져 있음. 
- 보관 기간이 끝나면 개인정보 삭제해야함. 
- 모든 달은 28일이며 오늘 날짜를 기준으로 함. 
- 오늘 파기할 개인정보 번호 구하기

A= 6 mon/ B= 12 mon/ C= 3mon

->
날짜를 일단위로 변환
기간을 일 단위로 변환
만료일 = 시작일+계약기간
"""


def timestamp(day):
    t = day.split(".")
    return (int(t[0]) * 12 * 28) + (int(t[1]) * 28) + int(t[2])


def solution(today, terms, privacies):
    answer = []
    terms_map = {}

    for i in terms:
        s = i.split(" ") #공백 분리
        terms_map[s[0]] = int(s[1]) * 28 - 1

    t = times(today)
    for i in range(len(privacies)):
        s = privacies[i].split(" ")
        d = times(s[0]) + terms_map[s[1]] #개인정보 만료일 계산
        # print(d, t)
        if d < t:
            answer.append(i + 1)  # 개인정보는 1번부터 시작하므로 i+1 추가

    return answer


