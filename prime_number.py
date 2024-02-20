# Prime Number Program in Python
# Check Whether a Number is a Prime or Not in Python
# Example
# Input : 11
# Output : 11 is a Prime
n = int(input())
flag = 0
if n < 2:
    flag = 1
    
for i in range(2,int((n/2)+1)):
    if n % i == 0:
        flag = 1
        break
    
if flag == 1:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
    
#By recursion method
num = int(input())
def checkPrime(num, iter=2):
    if num == iter:
        return True
    if num % iter == 0:
        return False
    if num < 2:
        return False
    return checkPrime(num, iter+1)

if checkPrime(num) == True:
    print("Prime")
else:
    print("Not Prime")