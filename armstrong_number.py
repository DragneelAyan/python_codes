# Armstrong Number in Python

# Check Whether a Given Number is an Armstrong Number or Not in Python
# Example
# Input : 371
# Output : It's an Armstrong Number
# Theory: 3**3 + 7**3 + 1**3 = 27 + 343 + 1 = 371
n = input()
p = len(n)
t = 0
for i in n:
    t = t + (int(i)**p)
    
if t == int(n):
    print("Armstrong")
else:
    print("Not Armstrong")