# cook your dish here
t = int(input())
for i in range(t):
    (a,b,c) = map(int, input().split(' '))
    L = []
    L.append(a)
    L.append(b)
    L.append(c)
    L.sort()
    s = L[1]
    print(s)