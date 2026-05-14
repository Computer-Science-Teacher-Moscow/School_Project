n = int(input())
finish_time = []
for _ in range(n):
    hours, minutes = map(int, input().split())
    finish_time.append([hours,minutes])
print(*min(finish_time))