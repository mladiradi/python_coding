
n = int(input())

positive_num = []
negative_num = []

for i in range(n):

    number = int(input())

    if number >= 0:
        positive_num.append(number)
    else:
        negative_num.append(number)

print(positive_num)
print(negative_num)
print(f"Count of positives: {len(positive_num)}")
print(f"Sum of negatives: {sum(negative_num)}")
