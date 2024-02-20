# Subtract lists element by element:
# a = [10, 15, 20, 30, 40]
# b = [5, 8, 20, 40, 25]
# a-b = [5, 7, 0, -10, 15]
a = [10, 15, 20, 30, 40]
b = [5, 8, 20, 40, 25]
c = []
for i in range(0,len(a)):
    c.append(a[i] - b[i])
print(c)