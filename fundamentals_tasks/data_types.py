
row1 = input()
row2 = input()


if row1 == "int":
    result = int(row2) * 2
elif row1 == "real":
    result = f"{float(row2) * 1.5:.2f}"
else:
    result = f"${row2}$"

print(result)
