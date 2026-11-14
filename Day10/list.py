'''
l = [[]]
if l: print('abc')
else: print('def')

l[start(0):end(len(l)):interval(1)]
#[1, 4, 16, 64, ...]
l = [i**2 for i in range(0, 20) if i % 2 == 0]
print(l)
print([1] + l[1:3:1] + [l[4]] + [l[8]])
l = [i for i in range(1, 101)]
a = l[0:10:1] #1-10
b = l[9:0:-1]+[l[0]] #10-1
c = [l[0]]+l[9:len(l):10] #1, 10, 20, ..., 100
d = l[0:len(l):3] #1, 4, 7, ..., 100
print(a,b,c,d, sep='\n')
l = [1,2,3,4,5]
print(l[::])

len(l) length -> len
max(l) maximum
min(l) minimum
sum(l)
l = [1, 2, 3, 4, 5]
print(max(l), min(l), sum(l))
#avg 小數後兩位
print(f'{sum(l)/len(l):.2f}')

新增 append()
移出 pop()
插入 insert(p, i)
刪除 remove(i) 
找位置 index(i)
找數量 count(i)
l = []
l.append(1) #對...做...
l.append(1) #對...做...
l.append(1) #對...做...
l.append(2)
l.append(3) #[1,2,3]
i = l.pop() #[1,2] 3
l.insert(1, 4) #[1,4,2]
l.remove(2) #[1,4]
idx = l.index(4) #1
c = l.count(1)
print(l, idx, c)

game_map = [
    ['','',''],A
    ['','',''],B
    ['','',''] C
     0. 1. 2
]

game_map = [A, B, C]
game_map[2] -> C
C[2] -> ''
game_map[2][2] -> ''

'''
game_map = [
    ['','',''],#a 0
    ['','',''],#b 1
    ['','',''] #c 2
]
#game_map = [a, b, c]
game = True#遊戲的狀態 正在玩/已結束
player = 'O'
while game:
    a, b = [int(i) for i in input().split()]
    if game_map[a][b]:
        print('Error')
        continue
    game_map[a][b] = player
    #橫
    for i in range(3):#i:0, 1, 2
        if game_map[i].count(player) == 3:
            print(f'{player} Won!')
            game = False
    #直
        # col = [game_map[0][0], game_map[1][0], game_map[2][0]]
        col = [game_map[j][i] for j in range(3)]
        if col.count(player) == 3:
            print(f'{player} Won!')
            game = False
    #斜
    l1 = [game_map[i][i] for i in range(3)]
    l2 = [game_map[i][2-i] for i in range(3)]
    for l in [l1, l2]:
        if l.count(player) == 3:
            print(f'{player} Won!')
            game = False
    
    if player == 'O': player = 'X'
    else: player = 'O'
    for row in game_map:
        print(row)

#平手 放置限制