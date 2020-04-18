
n, k = list(map(int, input().split()))
l = list()
count = 0

for _ in range(n):
    l.append(int(input()))
for i in l:
    if i % k == 0:
        count += 1
print(count)