
health = 100
bitcoins = 0
rooms = input().split('|')
i = 0

while True:
    if i == len(rooms):
        print("You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {health}")
        break

    room = rooms[i]
    command, number = room.split()
    number = int(number)

    if command == "potion":
        healed_amount = min(number, 100 - health)
        health += healed_amount
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}")
            break
    i += 1
