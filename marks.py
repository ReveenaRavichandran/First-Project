import datetime
class Student:
    def __init__(self,regno,name,dob,age,email,vote):
        self.regno=regno
        self.name=name
        self.dob=dob
        self.age=age
        self.email=email
        self.vote=vote
    def __str__(self):
        return f'{self.regno}\t{self.name}\t{self.dob}\t\t{self.age}\t{self.email}\t{self.vote}'
#     
s=[]
n=int(input("enter n:"))
for i in range(n):
    regno=int(input("enter regno"))
    name=input("enter name")
    dob=input("enter dob")
    d=datetime.datetime.now()
    age=int(d.strftime('%y'))-int(dob[9::])
    if age>=18:
        vote="yes"
    else:
        vote="no"

    email=str(regno)+"itech.edu"
    s.append(Student(regno,name,dob,age,email,vote))
    print=("regno",\t name","\t dob","\t age","\t\t email","\t eligible for vote")   
for i in s:
    print(i)
        

