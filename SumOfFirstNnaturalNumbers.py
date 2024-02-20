# Find the Sum of First N Natural Numbers
# Example
# Input : num = 8
# Output : 36

# Where first 8 number is 1, 2, 3, 4, 5, 6, 7, 8
# Sum of numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36

n = int(input())
total = 0
for i in range(0,n+1):
    total = total + i
    
print(total)