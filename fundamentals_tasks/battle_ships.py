
n = int(input())

field = []
for _ in range(n):
    row_str = list(map(int, input().split()))
    field.append(row_str)

attacks = input().split()
destroyed_ships = 0
destroyed_set = []

for attack in attacks:
    parts = attack.split('-')
    row = int(parts[0])
    col = int(parts[1])

    if 0 <= row < n and 0 <= col < len(field[row]):
        if field[row][col] > 0:
            field[row][col] -= 1
            if field[row][col] == 0 and (row, col) not in destroyed_set:
                destroyed_ships += 1
                destroyed_set.append((row, col))

print(destroyed_ships)
