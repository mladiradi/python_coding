
players = {}

while True:
    command = input().strip()
    if command == "Season end":
        break

    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}

        if position not in players[player] or players[player][position] < skill:
            players[player][position] = skill

    elif " vs " in command:
        player1, player2 = command.split(" vs ")

        if player1 in players and player2 in players:
            common_positions = set(players[player1].keys()).intersection(set(players[player2].keys()))

            if common_positions:
                total_skill1 = sum(players[player1].values())
                total_skill2 = sum(players[player2].values())

                if total_skill1 > total_skill2:
                    del players[player2]
                elif total_skill2 > total_skill1:
                    del players[player1]

sorted_players = sorted(players.items(), key=lambda p: (-sum(p[1].values()), p[0]))

for player, positions in sorted_players:
    total_skill = sum(positions.values())
    print(f"{player}: {total_skill} skill")

    sorted_positions = sorted(positions.items(), key=lambda pos: (-pos[1], pos[0]))
    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")
        