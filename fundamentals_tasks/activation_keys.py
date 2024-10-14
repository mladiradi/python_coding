
def contains(key, command):
    substring = command[1]
    if substring in key:
        return f"{key} contains {substring}"
    return "Substring not found!"


def flip(key, command):
    rule = command[1]
    start_index = int(command[2])
    end_index = int(command[3])
    left_string = key[:start_index]
    right_string = key[end_index:]

    if rule == 'Upper':
        sub_string = key[start_index: end_index].upper()  # взима символите между s и e_index и ги прави големи
        key = left_string + sub_string + right_string
    elif rule == 'Lower':
        sub_string = key[start_index: end_index].lower()
        key = left_string + sub_string + right_string
    return key


def slice(key, command):
    start_index = int(command[1])
    end_index = int(command[2])
    left_string = key[:start_index]
    right_string = key[end_index:]
    key = left_string + right_string
    return key


raw_key = input()
command = input()

while command != 'Generate':
    command = command.split('>>>')
    action = command[0]

    if action == 'Contains':
        print(contains(raw_key, command))
    elif action == 'Flip':
        raw_key = flip(raw_key, command)
        print(raw_key)
    elif action == 'Slice':
        raw_key = slice(raw_key, command)
        print(raw_key)
    command = input()

print(f"Your activation key is: {raw_key}")

# # input:
#
# abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate

# # output:
#
# abghijklmnopqrstuvwxyz
# abgHIJKLMNOPQRstuvwxyz
# abgHIjkLMNOPQRstuvwxyz
# Substring not found!
# Substring not found!
# Your activation key is: abgHIjkLMNOPQRstuvwxyz


# решение без функции:

activation_key = input()

while True:
    command = input()

    if command == 'Generate':
        break

    command = command.split('>>>')

    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == 'Flip':
        upper_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        start_string = activation_key[:start_index]
        end_string = activation_key[end_index:]
        change_part = activation_key[start_index:end_index]
        if upper_lower == 'Upper':
            activation_key = start_string + change_part.upper() + end_string
        elif upper_lower == 'Lower':
            activation_key = start_string + change_part.lower() + end_string
        print(activation_key)
    elif command[0] == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        start_string = activation_key[:start_index]
        end_string = activation_key[end_index:]
        delete_part = activation_key[start_index:end_index]
        activation_key = start_string + end_string
        print(activation_key)

print(f"Your activation key is: {activation_key}")
