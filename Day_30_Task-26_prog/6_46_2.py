with open('6_46_2.txt') as file:
    n, m = map(int, file.readline().split())
    teams = []
    planes = []
    for _ in range(n):
        teams.append(int(file.readline()))
    for _ in range(m):
        planes.append(int(file.readline()))
teams.sort(reverse=True)
planes.sort(reverse=True)
print(teams)
print(planes)
tickets = []
while planes and teams:
    plane = planes.pop(0)
    while teams:
        team = teams.pop(0)
        if team * 2 <= plane:
            tickets.append((team, plane))
            break
print(planes)
print(teams)
print(tickets)
print('----' * 50)
print(len(tickets), max(tickets)[0])


