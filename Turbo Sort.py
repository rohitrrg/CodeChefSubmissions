# cook your dish here
n = int(input())
L = []
for i in range(n):
    L.append(int(input()))
L.sort()
for i in L:
    print(i)