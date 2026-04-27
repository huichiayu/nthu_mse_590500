a = [1, 2, 3]
b = a          # NOT a copy
c = a.copy()   # shallow copy
a.append(4)
print(a, b, c)