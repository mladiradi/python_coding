
neighborhood = list(map(int, input().split('@')))
current_position = 0

while True:
    command = input()
    if command == "Love!":
        break
    parts = command.split()
    jump_length = int(parts[1])
    current_position += jump_length

    if current_position >= len(neighborhood):
        current_position = 0

    if neighborhood[current_position] > 0:
        neighborhood[current_position] -= 2

        if neighborhood[current_position] == 0:
            print(f"Place {current_position} has Valentine's day.")
    else:
        print(f"Place {current_position} already had Valentine's day.")

print(f"Cupid's last position was {current_position}.")

failed_places = sum(1 for hearts in neighborhood if hearts > 0)

if failed_places == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_places} places.")
