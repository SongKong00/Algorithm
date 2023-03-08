res = []
bag = []

N,M = map(int, input().split())

for Ncount in range(N):
    res.append(Ncount+1)

for Mcount in range(M):
    i, j = map(int, input().split())
    for num1 in range(i, j+1):
        bag.append(res[num1-1])
    for num2 in range(len(bag)):
        if j >= i:
            res[j-1] = bag[num2]
            j = j - 1
    bag =[]

for i in range(len(res)):
    print(res[i], end = " ")