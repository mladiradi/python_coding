
num_lst = list(map(int, input().split()))

while True:
    command = input()
    if command == "END":
        break
    parts = command.split()

    if parts[0] == "add" and parts[1] == "to" and parts[2] == "start":
        add = []

        for i in range(3, len(parts)):
            add.append(int(parts[i]))

        num_lst = add + num_lst

    elif parts[0] == "remove" and parts[1] == "greater" and parts[2] == "than":
        value = int(parts[3])
        left_nums = []

        for x in num_lst:
            if x <= value:
                left_nums.append(x)

        num_lst = left_nums

    elif parts[0] == "replace":
        value = int(parts[1])
        replacement = int(parts[2])

        for i in range(len(num_lst)):
            if num_lst[i] == value:
                num_lst[i] = replacement
                break

    elif parts[0] == "remove" and parts[1] == "at" and parts[2] == "index":
        index = int(parts[3])

        if 0 <= index < len(num_lst):
            num_lst.pop(index)

    elif parts[0] == "find" and parts[1] == "even":
        even = []
        for x in num_lst:
            if x % 2 == 0:
                even.append(x)
        print(" ".join(map(str, even)))

    elif parts[0] == "find" and parts[1] == "odd":
        odd = []
        for x in num_lst:
            if x % 2 != 0:
                odd.append(x)
        print(" ".join(map(str, odd)))

print(", ".join(map(str, num_lst)))
