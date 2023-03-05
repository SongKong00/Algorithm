h, m = input().split()
t = int(input())
h = int(h)
m = int(m)
minute = (h * 60) + m + t

h = int(minute / 60) % 24
m = minute % 60
print(h, m)