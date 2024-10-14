
pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())

while True:
    command = input()
    if command == "Retire":
        break
    parts = command.split()
    action = parts[0]

    if action == "Fire":
        index = int(parts[1])
        damage = int(parts[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif action == "Defend":
        start_index = int(parts[1])
        end_index = int(parts[2])
        damage = int(parts[3])

        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action == "Repair":
        index = int(parts[1])
        health = int(parts[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] = min(max_health, pirate_ship[index] + health)

    elif action == "Status":
        repair_threshold = 0.2 * max_health
        count = sum(1 for section in pirate_ship if section < repair_threshold)
        print(f"{count} sections need repair.")

pirate_ship_sum = sum(pirate_ship)
warship_sum = sum(warship)
print(f"Pirate ship status: {pirate_ship_sum}")
print(f"Warship status: {warship_sum}")
