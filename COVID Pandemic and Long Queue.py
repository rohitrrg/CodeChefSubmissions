t = int(input())
for i in range(t):
    n = int(input())
    L = [int(i) for i in input().split(' ')]

    indices = []

    flag = 1

    for i in range(len(L)):
        if L[i] ==1:
            indices.append(i)

    for i in range(len(indices)):
        if i < len(indices) - 1:
            if(indices[i+1]-indices[i]) < 6:
                flag = 0

    if (flag ==1):
        print('YES')
    else:
        print('NO')
