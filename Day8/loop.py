'''
for loop

for index in <range>
1.list
2.string
3.range()
l = [1,2,3]
for i in l:
    print(i)
l = ['鮭魚','鮪魚','玉子燒']
for shshi in l:
    print(shshi)
    if shshi == '鮭魚':print('拿') 
s = 'Hello'
for i in s:
    print(i)

range(start[init:0], end, interval[init:1])
from start -> end-1, += interval  

2, 4, 6, ..., 30
10, 9, 8, ..., 1
for i in range(10, 0, -1):
    print(i, end=' ')

for i in range(10):
    print(i, end=' ')
#continue(skip) break(stop)
for i in range(10):
    if i % 3 == 0: continue
    if i == 7:break
    print(i)
'''
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# [1, 2, 4, 8, 16, 32, 128, 256, 512]
# l = [2**i for i in range(10) if i != 6]
# print(l)
l = input().split()
print(l)
l = [int(i) for i in l]
print(l)