#Task
#Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

#Input Format
#A single integer, N (the argument to pass to factorial).

#Constraints
#2<=N<=12

#Output Format
#Print a single integer denoting N!.

#Solution

import math
import os
import random
import re
import sys

def factorial(n):
    if (n==1):
        return 1
    else:
        return (n*factorial(n-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)
