# Leap Year Program in Python
# Check if a Year is a Leap Year or Not in Python
# Example:
# Input : 2020
# Output : It's a Leap Year.

# Conditions for a Leap Year
# Here are the two conditions that any year must satisfy to be called a leap year
# 1. The year must be perfectly divisible by 400.
# 2. The number must be divisible by 4 but not by 100.
n = int(input())
if n % 400 == 0 or (n % 4 ==0 and n % 100 != 0):
    print("Leap Year")
else:
    print("Not a leap year")
    
#Using Ternary Operator
year = int(input())
def check_year(year):
    return ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))

print(f"{year} is a leap year" if check_year(year) else f"{year} is not a leap year")

#Using Lambda Function
year = int(input())
is_leap_year = lambda year: (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(f"{year} is a leap year" if is_leap_year(year) else f"{year} is not a leap year")