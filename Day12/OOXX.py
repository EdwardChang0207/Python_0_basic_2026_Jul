#Top-Down
def create_map():
    game_map = [['' for j in range(3)] for i in range(3)]
    return game_map

def va(a, b, game_map):
    if (a < 0) or (a >= 3) or (b < 0) or (b >= 3):
        return False
    if game_map[a][b]:
        return False
    return True

def draw(a, b, game_map, player):
    game_map[a][b] = player
    return game_map

def judge(game_map, player):
    for i in range(3):#i:0, 1, 2
            if game_map[i].count(player) == 3:
                return True
        #直
            # col = [game_map[0][0], game_map[1][0], game_map[2][0]]
            col = [game_map[j][i] for j in range(3)]
            if col.count(player) == 3:
                return True
        #斜
    l1 = [game_map[i][i] for i in range(3)]
    l2 = [game_map[i][2-i] for i in range(3)]
    for l in [l1, l2]:
        if l.count(player) == 3:
            return True

def change_player(player):
    if player == 'O': return 'X'
    else: return 'O'

def main():
    game_map = create_map()
    game = True
    player = 'O'
    while game:
        a, b = [int(i) for i in input().split()]
        if not va(a, b, game_map):
            continue
        game_map = draw(a, b, game_map, player)
        if judge(game_map, player):
            print(f'{player} Won!')
            game = False
        player = change_player(player)