list1 = list(map(int, input().strip().split(" ")))
counter = 0
num = list1[0]
for i in list1:
    freq = list1.count(i)
    if (freq > counter):
        counter = freq
        num = i
print(num)
