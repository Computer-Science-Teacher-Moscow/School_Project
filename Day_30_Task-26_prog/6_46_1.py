with open('6_46_1.txt') as file:
    k, n = int(file.readline()), int(file.readline())
    passengers = []
    # for _ in range(n):
    for s in file:
        #     start, end = map(int, file.readline().split())
        start, end = map(int, s.split())
        passengers.append((start, end))
passengers.sort()
print(passengers)
cells = [0] * k
print(cells)
cnt = 0
last_cell = 0
for start, end in passengers:
    for i, cell in enumerate(cells):
        if cell < start:
            cnt += 1
            last_cell = i + 1
            cells[i] = end
            print(i, cells)
            # input()
            break
print(cnt, last_cell)
