t = int(input())
for i in range(t):
    n = int(input())
    Max = 0

    for j in range(n):
        s,p,v = map(int,input().split())
        temp = (p//(s+1))*v
        Max = max(Max,temp)

    print(Max)

