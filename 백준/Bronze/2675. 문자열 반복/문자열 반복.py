num = int(input())
total = []
for i in range(num):
    repeat, S = map(str, input().split())
    for i in range(len(S)):
        total = total + [S[i] for j in range(int(repeat))]
    print(''.join(total))
    total = []