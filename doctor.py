class patient:
    def __init__(self,name,age,wgt,phone):
        self.name=name
        self.age=age
        self.wgt=wgt
        self.phone=phone
    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.wgt}\t{self.phone}'

class doctor:
    def __init__(self,docname,specialist):
        self.docname=docname
        self.specialist=specialist
    def __str__(self):
        return f'{self.docname}\t{self.specialist}'
    
p=[]
d=[]
n=int(input("Enter n:"))
for i in range(n):
    name=input("enter name")
    age=int(input("enter age:"))
    wgt=float(input("enter weight"))
    phone=input("enter mobile number")
    p.append(patient(name,age,wgt,phone))
p.sort(key=lambda x :x.wgt)
for i in p:
    print(i)
m=int(input("Enter m:"))
for i in range(m):
    docname=input("enter Doctor name")
    specialist=input("enter Specialist name")
    d.append(doctor(docname,specialist))
for j in d:
    print(j)

