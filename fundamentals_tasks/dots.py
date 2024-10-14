
n = int(input())
board = [input().split() for _ in range(n)]

max_connected_dots = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(len(board[i])):
        if board[i][j] == '.':
            stack = [(i, j)]
            connected_dots = 0

            while stack:
                row, col = stack.pop(0)

                if 0 <= row < n and 0 <= col < len(board[row]) and board[row][col] == '.':
                    board[row][col] = '-'
                    connected_dots += 1

                    for row_add, col_add in directions:
                        new_row = row + row_add
                        new_col = col + col_add
                        stack.append((new_row, new_col))

            if connected_dots > max_connected_dots:
                max_connected_dots = connected_dots

print(max_connected_dots)
