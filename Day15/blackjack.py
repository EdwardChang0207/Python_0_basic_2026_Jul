'''
A -> 1 or 11
2-9 -> 2-9
10/J/Q/K -> 10

game start: 2cards
while 還要 -> 再發一張
不要 -> 停止
**不可發出重複的牌**
寫出目前點數
if 點數 > 21:停牌
'''

def get_card():
    v = {'1':'A', '11': 'J', '12':'Q', '13':'K'}
    num = random.randint(1, 13)
    if str(num) in v.keys(): num = v[str(num)]

    suits = ['S', 'H', 'D', 'C']
    s = random.choice(suits)

    card = f'{s}{num}'
    return card

def cal_point(player):
    point1 = {"A":11, 'J':10, "Q":10, 'K':10}
    point2 = {"A":1, 'J':10, "Q":10, 'K':10}
    p1 = 0
    p2 = 0
    for card in player:
        num1 = card[1::]
        num2 = card[1::]
        if num1 in point1.keys():
            num1 = point1[num1]
            num2 = point2[num2]
        p1 += int(num1)
        p2 += int(num2)
    if p1 > 21: return p2
    if p1 > p2: return p1
    else: return p2

import random
game = True
# set() 集合 l = [1,1,2,2,2,3,3] -> s = {1,2,3}
player = set([get_card() for i in range(2)])
while len(player) < 2:
    card = get_card()
    if card not in player:
        player.add(player)
player = list(player)
print(player, cal_point(player))
while game:
    if input('Y/N:\n') == 'N':
        break
    card = get_card()
    while card in player:
        card = get_card()
    player.append(card)
    cur = cal_point(player)
    print(player, cur)
    if cur > 21:
        print('爆掉')
        break