n= int(input())

d=[0] *1001 #앞서 계산된 

d[1]= 1
d[2]= 3
for i in range(3, n+1):
  d[i] = (d[i-1] +2*[i-2]) % 796796


print(d[n]) #계산된 결과 출력
