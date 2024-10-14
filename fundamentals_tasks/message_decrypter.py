
import re

n = int(input())

for _ in range(n):
    text = input()
    pattern = r"^([\$%])([A-Z][a-z]{2,})\1: \[(\d+)]\|\[(\d+)]\|\[(\d+)]\|$"
    match = re.match(pattern, text)

    if match:
        tag = match.group(2)
        group1 = int(match.group(3))
        group2 = int(match.group(4))
        group3 = int(match.group(5))

        decrypted_message = chr(group1) + chr(group2) + chr(group3)

        print(tag + ": " + decrypted_message)
    else:
        print("Valid message not found!")
