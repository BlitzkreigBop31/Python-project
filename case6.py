y = int(input())
z = int(input())
for n in range(y, z + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)
