n = int(input())
a, b, c = 0, 0, 0

for i in range(1, n+1, 1):
    t = int(input())
    if t % 3 == 0: a = a+1
    elif t % 3 == 1: b = b+1
    else: c = c+1

print(a, b, c)