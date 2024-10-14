
n = int(input())
maze = [list(input()) for _ in range(n)]

start_row, start_col = None, None
for r in range(n):
    if 'k' in maze[r]:
        start_row, start_col = r, maze[r].index('k')
        break

queue = [(start_row, start_col, 1)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
longest_path = 0

while queue:
    row, col, dist = queue.pop(0)

    if row == 0 or row == n - 1 or col == 0 or col == len(maze[0]) - 1:
        longest_path = max(longest_path, dist)
    maze[row][col] = '#'

    for row_add, col_add in directions:
        new_row, new_col = row + row_add, col + col_add
        if 0 <= new_row < n and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == ' ':
            maze[new_row][new_col] = '#'
            queue.append((new_row, new_col, dist + 1))

if longest_path == 0:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {longest_path} moves")
