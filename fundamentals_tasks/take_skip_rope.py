
given_string = input()

numbers = []
non_numbers = []
for char in given_string:
    if char.isdigit():
        numbers.append(int(char))
    else:
        non_numbers.append(char)

take_lst = []
skip_lst = []
for index in range(len(numbers)):
    if index % 2 == 0:
        take_lst.append(numbers[index])
    else:
        skip_lst.append(numbers[index])

result = []
current_index = 0
for i in range(len(take_lst)):
    take = take_lst[i]
    skip = skip_lst[i]
    result.extend(non_numbers[current_index:current_index + take])
    current_index += take + skip

print("".join(result))
