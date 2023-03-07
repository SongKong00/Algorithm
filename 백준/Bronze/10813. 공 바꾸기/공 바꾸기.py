N, M = map(int, input().split())
result = [str(i+1) for i in range(N)]

for i in range(M) : 
    k, j = map(int, input().split())
    result[k-1], result[j-1] = result[j-1], result[k-1]

print(" ".join(result))