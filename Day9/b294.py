n = int(input())
l = input().split()
total = 0
for i in range(1, n+1):
    total = total + int(l[i-1]) * i
print(total)