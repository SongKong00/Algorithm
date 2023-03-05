h, m = input().split()
h = int(h)
m = int(m)
minute = (h * 60) + m - 45

if(minute < 0): minute = (24 * 60) + minute

h = int(minute / 60)
m = minute % 60
print(h, m)