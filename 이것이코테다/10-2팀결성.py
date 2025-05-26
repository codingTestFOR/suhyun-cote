"""
팀 결성 

학교에서 학생들에게 0번부터 N번까지의 번호 부여 
처음에는 모든 학생이 서로 다른팀으로 구분되어 N+1 개의 팀 존재 

M개의 연산 수행할 수 있을때 같은 팀 여부 확인 연산에 대한 연산결과 출력


"""


# 특정 원소가 속한 집합 찾기 (경로 압축 기법)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n: 학생 수, m: 연산 개수
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 부모 테이블 초기화

# 연산 수행
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)  # 팀 합치기
    elif op == 1:
        # 같은 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
