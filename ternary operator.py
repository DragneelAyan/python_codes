# Find the Greatest of the Three Numbers​ in Python
# Example
# Input : 20 30 10
# Output : 30
num1, num2, num3 = map(int, input().split())

max = num1 if num1 > num2 else num2
max = num3 if num3 > max else max
print(max)