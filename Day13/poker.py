'''
2 -> 2
A -> 1
Q -> 12
10 -> 10

Spades > Heart > Diamonds > Clubs

SA HA -> SA
S10 S8 -> S10
C10 S3 -> C10

2 45 60
67 78 80

隨機發牌
S10 D8 -> S10
random
random.randint(a, b)
random.choice([])

'''

# value = {'A':1,'J':11,'Q':12,'K':13}
import random
g1 = [2, 45, 60]
g2 = [67,78, 80]
print(random.choice(g1))
print(random.choice(g2))
