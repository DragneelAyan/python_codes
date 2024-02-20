# Sum of Numbers in a given Range in Python
# Example
# Input : 2 5
# Output : 14
a, b = map(int, input().split())
total = 0
for i in range(a, b+1):
    total = total + i
    
print(total)