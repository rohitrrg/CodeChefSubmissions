# cook your dish here
T = int(input())

for i in range(T):
    N = int(input())
    mat = []
    for i in range(N):
        val = int(input())
        mat.append(val)
    print(max(mat))
