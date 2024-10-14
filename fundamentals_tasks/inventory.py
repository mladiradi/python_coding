
journal = input()
inventory = journal.split(", ")

while True:
    command = input()

    if command == "Craft!":
        break

    parts = command.split(" - ")
    action = parts[0]

    if action == "Collect":
        item = parts[1]
        if item not in inventory:
            inventory.append(item)

    elif action == "Drop":
        item = parts[1]
        if item in inventory:
            inventory.remove(item)

    elif action == "Combine Items":
        old_item, new_item = parts[1].split(":")
        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(index + 1, new_item)

    elif action == "Renew":
        item = parts[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

print(", ".join(inventory))
