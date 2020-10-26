#Task
#Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. 
#The constructor must assign initialAge to age after confirming the argument passed as  is not negative; if a negative argument is passed as initialAge, 
#the constructor should set age to 0 and print "Age is not valid, setting age to 0.". In addition, you must write the following instance methods:

# 1. yearPasses() should increase the age instance variable by 1.
# 2. amIOld() should perform the following conditional actions:
#    If age<13, print You are young..
#    If age>=13 and age<18, print You are a teenager..
#    Otherwise, print You are old..

#The code that creates each instance of your Person class is in the main method.

#Input Format
#The first line contains an integer, t (the number of test cases), and the t subsequent lines each contain an integer denoting the  of a Person instance.

#Constraints
#1<=t<=4
#-5<=age<=30

#Output Format
#If your methods are implemented correctly, each test case will print 2 or 3 lines (depending on whether or not a valid initialAge was passed to the constructor).

#Solution

class Person:
    def __init__(self,initialAge):
        if(initialAge>0):
            self.age=initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age=0
    def amIOld(self):
        if(self.age < 13):
            print("You are young.")
        elif(self.age >=13 and self.age<18):
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age=self.age+1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
