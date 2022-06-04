y = input()
ascii = []
list1 = []
for ele in y:
    ascii.append(ord(ele))
ascii.sort()
for x in ascii:
    list1.append(chr(x))
print(list1)
