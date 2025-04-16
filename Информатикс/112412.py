K, M, B = map(int, input().split())
N = int(input())
selected_players = []
for _ in range(N):
    surname, name, year, goals = input().split()
    year = int(year)
    goals = int(goals)

    if K <= year <= M and goals == B:
        selected_players.append(f"{surname} {name}")

for player in selected_players:
    print(player)

print(len(selected_players))
