a = []
n = 100
l = 0
for i in range(0, n):
    l += int(input())
print(l - (n * (n - 1) / 2))
