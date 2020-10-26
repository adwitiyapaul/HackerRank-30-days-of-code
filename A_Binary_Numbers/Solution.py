#Task
#Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

#Input Format
#A single integer, n.

#Constraints
#1<=n<=10^6

#Output Format
#Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

#Solution

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

result=0
maximum=0

while (n>0):
    if (n%2==1):
        result+=1
        if (result>maximum):
            maximum = result
    else:
        result=0
        
    n=n//2 
print(maximum)
