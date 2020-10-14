#Simple Tic Tac Toe game
import itertools


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

#Horizontal Winner
    for row in current_game:
        #print(row)
        if all_same(row):
            print()
            print(f"Player {row[0]} is the winner Horizontally (--) !")
            return True

#Vertical Winner
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            #print(row[0])
            check.append(row[col])
        if all_same(check):
            print()
            print(f"Player {check[0]} is the winner Vertically (|) !")
            return True

#Diagonal Winner
    dia = []
    for ix in range(len(current_game)):
        dia.append(current_game[ix][ix])
    if all_same(dia):
            print(f"Player {dia[0]} is the winner Diagonally (\) !")
            return True
    #print(dia)

    dia = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        #print(col, row)
        dia.append(current_game[row][col])
    if all_same(dia):
            print(f"Player {dia[0]} is the winner Diagonally (/) !")
            return True
    #print(diag)
    return False


def game_board( game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print()
            print("Oops! position is occupied, Choice another!")
            print("-------------------------------------------------")
            return game_map, False
        if player != 0:
            game_map[row][column] = player
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate(game_map):
            print(count, row)
        print()
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2!", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


play = True
players = [1,2]
while play:
    game_size = int(input("What size of tic tac toe? " ))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")

        played = False
        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            print()
            again = input("Would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting...")
            elif again.lower() == "n":
                print("Byeeeee")
                play = False
            else:
                print("Not a valid answer, so.... c u ltr aligator ")
                play = False