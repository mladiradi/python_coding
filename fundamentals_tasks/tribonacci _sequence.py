
n = int(input())
sequence = []

for i in range(n):
    if i == 0:
        sequence.append(1)
    elif i == 1:
        sequence.append(1)
    elif i == 2:
        sequence.append(2)
    else:
        next_term = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_term)

print(" ".join(map(str, sequence)))
