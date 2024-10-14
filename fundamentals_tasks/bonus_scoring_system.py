import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for _ in range(number_of_students):
    attendances = int(input())
    if number_of_lectures > 0:
        total_bonus = attendances / number_of_lectures * (5 + additional_bonus)
    else:
        total_bonus = 0

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = attendances

max_bonus = math.ceil(max_bonus)

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendance} lectures.")
