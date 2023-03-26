Enst = []
a = int(input())
for i in range(a):
    b = int(input())
    if b == 3 or b == 4 or b == 5:
        Enst.append(b)
print((len(Enst) / a) * 100)