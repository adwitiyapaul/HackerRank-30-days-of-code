#Task
#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
#and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

#Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

#Input Format
#There are 3 lines of numeric input:
#The first line has a double, meal_cost (the cost of the meal before tax and tip).
#The second line has an integer, tip_percent (the percentage of  being added as tip).
#The third line has an integer, tax_percent (the percentage of  being added as tax).

#Output Format
#Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).

#Solution:

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip=meal_cost*(tip_percent/100)
    tax=meal_cost*(tax_percent/100)
    total_cost=meal_cost+tip+tax
    r=int(round(total_cost))
    print(r)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
