#Task
#Given a string, S, of length  that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings 
#on a single line (see the Sample below for more detail).

#Note: 0 is considered to be an even index.

#Input Format
#The first line contains an integer, T (the number of test cases).
#Each line i of the T subsequent lines contain a String, S.

#Constraints
#1<=T<=10
#2<=length of S<=10000

#Output Format
#For each String Sj (where 0<=j<=T-1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.

#Solution

t=int(input().strip())
s=[]

for i in range (t):
    a=input().strip()
    s.append(a)

for i in s:
    str1=[]
    str2=[]
    str=list(i)
    for j in range (len(str)):
        if (j%2==0):
            str1.append(str[j])
        else:
            str2.append(str[j])
    p=""
    q=""
    p=p.join(str1)
    q=q.join(str2)
    print(p,q)
