N, M = map(int, input().split())
result = [0 for i in range(N)]

for i in range(M) : 
    setting = list(map(int, input().split()))
    for i in range(setting[0], setting[1] + 1):
        result[i-1] = setting[2]

for i in range(N):
    print(result[i], end=" ")