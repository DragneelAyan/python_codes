n = int(input())
a = 0
b = 1
flist = []
k = 0
for i in range(0, n):
    flist.append(a)
    c = a + b
    a = b
    b = c
    
for i in range(0, len(flist)):
    k = k + flist[i]
    
print(k)