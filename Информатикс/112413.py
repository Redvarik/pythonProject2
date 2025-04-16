N = int(input())
players = []

for _ in range(N):
    surname, name, year, goals = input().split()
    goals = int(goals)
    players.append((surname, name, goals))

max_goals = max(player[2] for player in players)

for player in players:
    if player[2] == max_goals:
        print(f"{player[0]} {player[1]}")


print(max_goals)
