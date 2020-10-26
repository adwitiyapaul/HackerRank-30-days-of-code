#Task
#You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
#Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

#A Student class constructor, which has 4 parameters:
#A string, firstName.
#A string, lastName.
#An integer, id.
#An integer array (or vector) of test scores, scores.
#A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
#Grading Scale
#   Letter    Average(a)
#     O       90<=a<=100  
#     E        80<=a<90
#     A        70<=a<80
#     P        55<=a<70
#     D        40<=a<55
#     T         a<40

#Input Format
#The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

#Constraints
#1<=|firstName|,|lastName|<=10
#id==7
#0<=score,average<=100

#Output Format
#This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

#Solution

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, testScores):
        super().__init__(firstName, lastName, idNumber)
        self.testScores = testScores
    def calculate(self):
        total = 0
        for testScore in self.testScores:
            total += testScore
        avg = total / len(self.testScores)
        if 90 <= avg <= 100:
            return 'O'
        if 80 <= avg < 90:
            return 'E'
        if 70 <= avg < 80:
            return 'A'
        if 55 <= avg < 70:
            return 'P'
        if 40 <= avg < 55:
            return 'D'
        return 'T'
   
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
