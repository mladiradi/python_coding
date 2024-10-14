
shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split()
    action, product = command[0], command[1]

    if action == "Urgent":
        if product not in shopping_list:
            shopping_list.insert(0, product)

    elif action == "Unnecessary":
        if product in shopping_list:
            shopping_list.remove(product)

    elif action == "Correct":
        new_product = command[2]
        if product in shopping_list:
            index = shopping_list.index(product)
            shopping_list[index] = new_product

    elif action == "Rearrange":
        if product in shopping_list:
            shopping_list.remove(product)
            shopping_list.append(product)

print(', '.join(shopping_list))
