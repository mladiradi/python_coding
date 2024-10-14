
population = list(map(int, input().split(", ")))
min_wealth = int(input())

total_wealth = sum(population)
basis_wealth = len(population) * min_wealth

if total_wealth < basis_wealth:
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            needed = min_wealth - population[i]

            for j in range(len(population)):
                richest_i = 0
                for k in range(1, len(population)):
                    if population[k] > population[richest_i]:
                        richest_i = k

                if population[richest_i] > min_wealth:
                    transfer = min(needed, population[richest_i] - min_wealth)
                    population[i] += transfer
                    population[richest_i] -= transfer
                    needed -= transfer

                if needed == 0:
                    break

    print(population)
