# Find the Armstrong Numbers in a given Range in Python
# Input : 150 160
# Output : 153
# Theory: 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153
a, b = map(int, input().split())

def check_armstrong(num):
    p = len(str(num))
    t = 0
    for i in str(num):
        t = t + (int(i)**p)
    if t == num:
        return True
        
arm = []
for i in range(a, b+1):
    if check_armstrong(i) == True:
        arm.append(i)

print(arm)