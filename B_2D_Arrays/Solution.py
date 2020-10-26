#Context
#Given a 6x6 2D Array, A:
#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0

#We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
#a b c
#  d
#e f g
#There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

#Task
#Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

#Input Format
#There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of -9 to 9.

#Constraints
#-9<=A[i][j]<=9
#0<=i,j<=5

#Output Format
#Print the largest (maximum) hourglass sum found in A.

#Solution

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

maximum = -9 * 7

for i in range(6):
    for j in range(6):
        if j + 2 < 6 and i + 2 < 6:
            result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if result > maximum:
                maximum = result

print(maximum)
