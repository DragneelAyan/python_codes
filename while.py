age = int(input())
agelimit = list(range(18,81))

while age not in agelimit:
    print("Enter a proper age")
    age = int(input())
    
print(f"Age entered: {age}")