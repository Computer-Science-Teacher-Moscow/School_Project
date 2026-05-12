with open('6_48_4.txt') as file:
    k, n = int(file.readline()), int(file.readline())
    hairdressers = [set()] * k
    clients = []
    for s in file:
        start_time, end_time = map(int, s.split())
        clients.append(set(range(start_time, end_time + 1)))
cnt = 0
last_hairdresser = 0
penultimate_hairdressers = 0
for r in clients:
    for i, hd_r in enumerate(hairdressers):
        if r & hd_r == set():
            hairdressers[i] = r | hd_r
            cnt += 1
            penultimate_hairdressers = last_hairdresser
            last_hairdresser = i + 1
            break
print(cnt, penultimate_hairdressers)