import datetime
def getmarks():
    n=int(input("enter n:"))
    i=0
    while i<n:
        mark=int(input('Enter a Mark:'))
        name=input('Enter a Name:')
        dob =input("Enter a Date of brith:")
        age=int(dob[6::])
        s=datetime.datetime.now()
        s=int(s.strftime("%Y"))
        age=s-age
        if(mark>0 and mark<=100 and age >=14):
            l.append(mark)
        i=i+1
    print(l)
 
def passeddetails():
    for i in l:
        if i>=50:
            pd.append(i)
    print("\t***Passed details***")
    for i in pd:
        print(i)
def faileddetails():
    for i in l:
       if i<=50:
           fd.append(i)
    print("\t***failed details*** ")
    for j in fd:
        print(i)
def highlowmarks():
    max=0
    for i in pd:
        if i<max:
            max=i
    print("Highesh mark :",max)
    min=50
    for i in fd:
        if i<min:
            min=i
    print("lower mark :",min)
def passrate():
    pr=len(pd)/len(l)*100
    print("pass rate :",pr)
l=[]
pd=[]
fd=[]
getmarks()
passeddetails()
faileddetails()
highlowmarks()
passrate()
