game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def game_board( game_map, player=0, row=0, column=0, just_display=False):
    try:
        if player != 0:
            game_map[row][column] = player
        print("   0  1  2")
        for count, row in enumerate(game_map):
            print(count, row)
        print()
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2!", e)
    except Exception as e:
        print("Something went very wrong!", e)


game = game_board(game, just_display=True)
game = game_board(game, 1,2,1)