# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    s_rev=list(reversed(s))
    print(int("".join(map(str,s_rev))))
