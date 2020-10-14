game = [[2,0,1],
        [0,1,0],
        [1,1,2]]

def win(current_game):
#Horizontal Winner
    for row in current_game:
        #print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print()
            print(f"Player {row[0]} is the winner Horizontally (--) !")

#Vertical Winner
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            #print(row[0])
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print()
            print(f"Player {check[0]} is the winner Vertically (|) !")

#Diagonal Winner
    dia = []
    for ix in range(len(current_game)):
        dia.append(current_game[ix][ix])
    if dia.count(dia[0]) == len(dia) and dia[0] != 0:
            print(f"Player {dia[0]} is the winner Diagonally (\) !")
    #print(dia)

    dia = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        #print(col, row)
        dia.append(current_game[row][col])
    if dia.count(dia[0]) == len(dia) and dia[0] != 0:
            print(f"Player {dia[0]} is the winner Diagonally (/) !")
    #print(diag)

win(game)