# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    if (n >= 100):
        sum = int(n / 100) + sum
        n = int(n % 100)
    if (n >= 50):
        sum = int(n / 50) + sum
        n = int(n % 50)
    if (n >= 10):
        sum = int(n / 10) + sum
        n = int(n % 10)
    if (n >= 5):
        sum = int(n / 5) + sum
        n = int(n % 5)
    if (n >= 2):
        sum = int(n / 2) + sum
        n = int(n % 2)
    if (n == 1):
        sum = 1 + sum
        n = 1

    print(sum)