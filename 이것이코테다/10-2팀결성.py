"""
팀 결성 

학교에서 학생들에게 0번부터 N번까지의 번호 부여 
처음에는 모든 학생이 서로 다른팀으로 구분되어 N+1 개의 팀 존재 

M개의 연산 수행할 수 있을때 같은 팀 여부 확인 연산에 대한 연산결과 출력


"""


def find_parent(parent, x):
    if parent[x] !=x:
        parent[x]= find_parent(parent,parent[x])

    return parent[x]
