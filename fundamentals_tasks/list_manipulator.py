
initial_list = list(map(int, input().strip().split()))

while True:
    command = input().strip()
    if command == "end":
        break

    parts = command.split()
    action = parts[0]

    if action == "exchange":
        index = int(parts[1])
        if 0 <= index < len(initial_list):
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]
        else:
            print("Invalid index")

    elif action == "max" or action == "min":
        even = parts[1] == "even"
        rightmost = -1

        for i in range(len(initial_list)):
            if (initial_list[i] % 2 == 0) == even:
                if rightmost == -1 or \
                   (action == "max" and initial_list[i] >= initial_list[rightmost]) or \
                   (action == "min" and initial_list[i] <= initial_list[rightmost]):
                    rightmost = i

        if rightmost == -1:
            print("No matches")
        else:
            print(rightmost)

    elif action == "first" or action == "last":
        count = int(parts[1])
        if count > len(initial_list):
            print("Invalid count")
        else:
            even = parts[2] == "even"
            filtered = []
            for x in initial_list:
                if (x % 2 == 0) == even:
                    filtered.append(x)

            if action == "first":
                result = filtered[:count]
            else:  # action == "last"
                result = filtered[-count:]

            print(result)

print(initial_list)
