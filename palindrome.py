# Palindrome Program in Python
# Example
# Input : 1221
# Output : Palindrome
s = input()
rs = s[::-1]
if s == rs:
    print("Palindrome")
else:
    print("Not palindrome")