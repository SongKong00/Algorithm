N = int(input())

list = list(map(int, input().split()))

find = int(input())
count = 0

for i in range(N):
    if list[i] == find :
        count += 1
        
print(count)