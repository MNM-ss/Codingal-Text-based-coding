coordinates = list(map(int, input().split()))
k = int(input())

count = 0
for i in range(5):
    for j in range(i + 1, 5):
        if abs(coordinates[i] - coordinates[j]) <= k:
            count += 1

print(count)
