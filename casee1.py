n = int(input())
x = []
for i in range(0, n):
    ele = int(input())
    x.append(ele)

y = input()
if (y == "asc"):
    x.sort()
    print(x)

if (y == "desc"):
    x.sort(reverse=True)
    print(x)
if (y == "none"):
    x = x
    print(x)
