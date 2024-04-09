N = int(input())
num = []

for _ in range(N):
    x, y = map(int, input().split())
    num.append((x, y))

num.sort(key=lambda point: (point[0], point[1]))

for point in num:
    print(point[0], point[1])
