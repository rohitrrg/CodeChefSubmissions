# cook your dish here
t = int(input())
k = list(map(int, input().split(' ')))
odd = 0
even =0
for i in range(t):
    if(k[i]%2==0):
        even = even+1
    else:
        odd = odd+1
if(even>odd):
    print('READY FOR BATTLE')
else:
    print('NOT READY')