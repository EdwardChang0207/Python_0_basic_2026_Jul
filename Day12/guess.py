'''
ans -> 正確答案
upper, lower -> 上、下界
guess -> 玩家猜測的
cnt -> 猜的次數

在玩家猜到答案以前，遊戲繼續
猜中之後，要寫出答案&猜了幾次
'''
import random
ans = random.randint(1, 100)
lower, upper = 1, 100
cnt = 0
game = True
#遊戲開始
while game:
    #寫出範圍
    print(f'{lower}~{upper}')
    #玩家輸入
    guess = int(input())
    cnt += 1
    if (guess < lower) or (guess > upper): continue
    #驗證答案
    if guess == ans:
        #答對 -> 遊戲結束
        print(f'the answer is {ans}, you have guess {cnt} times')
        game = False
    elif guess > ans:
        print('too big!')
        upper = guess
    else:
        print('too small')
        lower = guess
        #答錯 -> 修正上下界
#顯示結果