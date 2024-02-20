# Sum of Digits of a Number in Python
# Example
# Input : number = 123
# Output : 6
n = int(input())
n = str(n)
total = 0
for i in n:
    total = total + int(i)
    
print(total)

#Using Recursion
n = int(input())
def findSum(n):
    if n == 0:
        return 0
    return int((n%10) + findSum(n/10))
    
print(findSum(n))

#Cool method
n = [int(d) for d in input("Enter number:")]
print("Sum of digits is:", sum(n))