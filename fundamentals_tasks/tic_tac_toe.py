tic = list(map(int, input().split()))
tac = list(map(int, input().split()))
toe = list(map(int, input().split()))

board = [tic, tac, toe]
winner = 0

for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != 0:
        winner = board[i][0]
        break

if winner == 0:
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            winner = board[0][i]
            break

if winner == 0:
    if board[0][0] == board[1][1] == board[2][2] != 0:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        winner = board[0][2]

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
