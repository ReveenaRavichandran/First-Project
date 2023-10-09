n=int(input("enter n:"))
l=[]
p=[]
f=[]
i=0
while i<n:
    mark=int(input('Enter a Mark:'))
    name=input('Enter a Name:')
    age=int(input("Enter a Age:"))
    print("****")
    r=[]
    if(mark>0 and mark<=100 and age >=14):
        r.append(mark)
        r.append(name)
        r.append(age)
        l.append(r)
        i=i+1
for i in l:
    if i[0] >=50:
        p.append(i)
    else:
        f.append(i)
print("Passed mark")
for j in l:
    for i in p:
        if j[0] == i[0]:
            print(i)
print("Failed Mark")
for i in f:
    print(i,sep="\t",end="\n")
big=50
for i in p:
    if i[0]>big:
        big=i[0]
print("Highesh mark :",big)
low=50
for i in f:
    if i[0]<low:
        low=i[0]
print("lower mark :",low) 

print("Pass rate : ", len(p)/n*100)

    
        
 
