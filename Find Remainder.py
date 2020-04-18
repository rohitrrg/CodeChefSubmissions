T = int(input())
for tc in range(T):
    # Read integers a and b.
    (a, b) = map(int, input().split(' '))

    # Compute the answer
    # Complete the line below
    ans = a % b
    print(ans)