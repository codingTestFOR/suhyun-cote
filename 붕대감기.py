def solution(bandage, health, attacks):
    t, x, y = bandage  # 붕대 감기 시간, 초당 회복량, 추가 회복량
    max_health = health  # 최대 체력
    current_health = health  # 현재 체력
    attack_times = {time: damage for time, damage in attacks}  # 공격 정보를 딕셔너리로 저장
    success_time = 0  # 연속 붕대 감기 성공 시간
    
    last_attack_time = attacks[-1][0]  # 마지막 공격 시간
    
    for time in range(last_attack_time + 1):  # 0초부터 마지막 공격 시간까지 진행
        if time in attack_times:
            # 몬스터 공격 받음
            current_health -= attack_times[time]
            success_time = 0  # 붕대 감기 초기화
            if current_health <= 0:
                return -1  # 캐릭터 사망
        else:
            # 붕대 감기 시전
            success_time += 1
            current_health += x  # 기본 회복량 적용
            if success_time == t:
                current_health += y  # 추가 회복량 적용
                success_time = 0  # 연속 성공 초기화
            
            # 최대 체력 초과 방지
            current_health = min(current_health, max_health)
    
    return current_health
