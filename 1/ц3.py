a = input()
b = "=?*^$№@_"
c = ""
for i in a:
    if i in b:
        c = c + i
print(c)