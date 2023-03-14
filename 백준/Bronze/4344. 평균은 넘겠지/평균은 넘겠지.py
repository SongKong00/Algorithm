C = int(input())
count = 0
for i in range(C):
    test_case = list(map(int, input().split()))
    avg = (sum(test_case) - test_case[0]) / test_case[0]
    for i in range(1,test_case[0]+1):
        if test_case[i] > avg:
            count = count + 1
    print(f'{count/test_case[0]*100:.3f}%')
    avg = 0
    test_case = []
    count = 0