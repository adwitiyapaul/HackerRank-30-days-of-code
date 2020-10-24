#Task
#Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

#Input Format
#The first line contains an integer, N (the size of our array).
#The second line contains N space-separated integers describing array A's elements.

#Constraints
#1<=N<=1000
#1<=Ai<=1000, where Ai is the ith integer in the array.

#Output Format
#Print the elements of array  in reverse order as a single line of space-separated numbers.

#Solution

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

a=list(reversed(arr))

for i in a:
    print(i,end=' ');
