str1 = input().split()
num = 0
print(str1)
for i in str1:
    i = str(i)
    for c in i:

        if c.isdigit():
            c = int(c)
            num += c
print(num)
