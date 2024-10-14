
painting_lst = list(map(int, input().split()))

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()

    if parts[0] == "Change":
        painting_number = int(parts[1])
        new_number = int(parts[2])

        if painting_number in painting_lst:
            index = painting_lst.index(painting_number)
            painting_lst[index] = new_number

    elif parts[0] == "Hide":
        painting_number = int(parts[1])

        if painting_number in painting_lst:
            painting_lst.remove(painting_number)

    elif parts[0] == "Switch":
        painting_1 = int(parts[1])
        painting_2 = int(parts[2])

        if painting_1 in painting_lst and painting_2 in painting_lst:
            painting1 = painting_lst.index(painting_1)
            painting2 = painting_lst.index(painting_2)
            painting_lst[painting1], painting_lst[painting2] = painting_lst[painting2], painting_lst[painting1]

    elif parts[0] == "Insert":
        index = int(parts[1])
        painting_number = int(parts[2])

        if 0 <= index < len(painting_lst):
            painting_lst.insert(index + 1, painting_number)

    elif parts[0] == "Reverse":
        painting_lst.reverse()

print(" ".join(map(str, painting_lst)))
