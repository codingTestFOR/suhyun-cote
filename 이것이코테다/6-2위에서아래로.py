n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True) 

for i in array:
    print(i, end=' ')


----

n = int(input())  
array = [int(input()) for _ in range(n)]  
array.sort(reverse=True)  
print(*array)  
