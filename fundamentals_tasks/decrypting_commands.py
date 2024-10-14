

# == 2.1. World Tour

decrypt_message = input()

while True:
    command = input()
    if command == "Finish":
        break
    command = command.split()
    action = command[0]
    if action == "Replace":
        current_char = command[1]
        new_char = command[2]
        decrypt_message = decrypt_message.replace(current_char, new_char)
        print(decrypt_message)

    elif action == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(decrypt_message) and start_index <= end_index < len(decrypt_message):
            decrypt_message = decrypt_message[:start_index] + decrypt_message[end_index + 1:]
            print(decrypt_message)
        else:
            print("Invalid indices!")

    elif action == "Make":
        letter = command[1]
        if letter == "Upper":
            decrypt_message = decrypt_message.upper()
        elif letter == "Lower":
            decrypt_message = decrypt_message.lower()
        print(decrypt_message)

    elif action == "Check":
        given_string = command[1]
        if given_string in decrypt_message:
            print(f"Message contains {given_string}")
        else:
            print(f"Message doesn't contain {given_string}")

    elif action == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(decrypt_message) and start_index <= end_index < len(decrypt_message):
            substring = decrypt_message[start_index: end_index + 1]
            substring_sum = sum(ord(char) for char in substring)
            print(substring_sum)
        else:
            print("Invalid indices!")
