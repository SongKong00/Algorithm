word = list(input())
compareS = list('abcdefghijklmnopqrstuvwxyz')
compareL = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
count = [0 for i in range(len(compareL))]

for i in range(len(word)):
    for j in range(len(compareL)):
        if word[i] == compareL[j]:
            count[j] = count[j] + 1
    for k in range(len(compareS)):
        if word[i] == compareS[k]:
            count[k] = count[k] + 1

if count.count(max(count)) > 1:
    print('?')
else:
    print(compareL[count.index(max(count))])