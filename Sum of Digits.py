t = int(input())

for i in range(t):
    n = int(input())
    a = 0
    while(n>0):
        b = int(n%10)
        a = int(a+b)
        n = int(n/10)
    print(a)