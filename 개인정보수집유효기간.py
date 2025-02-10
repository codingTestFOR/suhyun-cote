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


def get_day(ymd):
    y, m, d = map(int, ymd.split('.'))
    return (y * 12 * 28) + (m * 28) + d  # 날짜를 일 단위로 변환

def solution(today, terms, privacies):
    answer = []
    today_days = get_day(today) 
    
    term_dict = {}
    for term in terms:
        t_type, t_months = term.split()
        term_dict[t_type] = int(t_months) * 28  # 기간을 일 단위로 변환

    for i, privacy in enumerate(privacies):
        date, p_type = privacy.split()
        expiry_date = get_day(date) + term_dict[p_type]  # 만료일 계산
        
        if expiry_date <= today_days:  # 오늘 날짜와 비교
            answer.append(i + 1)

    return answer

