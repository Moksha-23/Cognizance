#creating table
n=int(input('Enter The Number of Students : '))
a=[['Roll No','Name','Marks']]
for i in range(n):
    roll=input('Enter Roll No : ')
    studentname=input('Enter Student Name : ')
    marks=int(input('Enter Marks : '))
    a.append([roll,studentname,marks])
for i in range(len(a)):
    for j in range(len(a[i])):
        k=a[i][j]
        print(k,end='\t')
    print('\n')
h=int(input('Enter The Row to be Printed : '))
for i in a[h]:
    print(i,end='\t')