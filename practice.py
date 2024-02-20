import math
import os
import random
import re
import sys



#
# Complete the 'calc' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER c as parameter.
#

def calc(c):
    # Write your code here
    pi = math.pi
    radius = c/(2*pi)
    area = pi * (radius**2)
    print(radius, area)

if __name__ == '__main__':

    c = int(input())

    result = calc(c)
