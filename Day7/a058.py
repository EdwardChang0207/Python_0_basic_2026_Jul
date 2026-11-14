n = int(input())
a, b, c = 0, 0, 0
i = 0
while i < n:
    #判斷一個數字
    t = int(input())
    if t % 3 == 0:
        a = a + 1
    elif t % 3 == 1:
        b = b + 1
    else:
        c = c + 1
    i = i + 1
print(a, b, c)
