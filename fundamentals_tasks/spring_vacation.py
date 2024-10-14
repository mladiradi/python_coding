days = int(input())
budget = float(input())
number_of_people = int(input())
fuel_price_per_km = float(input())
food_expense_per_person_per_day = float(input())
accommodation_price_per_person = float(input())

total_food_expense = days * food_expense_per_person_per_day * number_of_people

if number_of_people > 10:
    total_accommodation_expense = days * accommodation_price_per_person * number_of_people * 0.75
else:
    total_accommodation_expense = days * accommodation_price_per_person * number_of_people

total_expenses = total_food_expense + total_accommodation_expense

for day in range(1, days + 1):
    traveled_distance = float(input())
    daily_fuel_expense = traveled_distance * fuel_price_per_km
    total_expenses += daily_fuel_expense

    if day % 3 == 0 or day % 5 == 0:
        total_expenses += total_expenses * 0.4

    if day % 7 == 0:
        total_expenses -= total_expenses / number_of_people

    if total_expenses > budget:
        deficit = total_expenses - budget
        print(f"Not enough money to continue the trip. You need {deficit:.2f}$ more.")
        break
else:
    remaining_budget = budget - total_expenses
    print(f"You have reached the destination. You have {remaining_budget:.2f}$ budget left.")
