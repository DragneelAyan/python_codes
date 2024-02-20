# Python program to find factors of a number
# Example1
# Input : 10
# Output : 2 5
# Example2
# Input: 100
# Output: 1 2 4 5 10 20 25 50 100
n = int(input())
factors = []
for i in range(1,n+1):
    if n%i == 0:
        factors.append(i)
print(factors)