# Fibonacci Series in Python
# Example
# Input : 4
# Output : 0 1 1 2
n = int(input())
a = 0
b = 1
pallist = []
for i in range(n+1):
    pallist.append(a)
    c = a + b
    a = b
    b = c
    
print(pallist)