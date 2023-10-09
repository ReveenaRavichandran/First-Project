from statistics import *
from datetime import *
from random import *
from math import *
def myrand(sr,er):
    for i in range(sr,er):
        l.append(randint(sr,er))
    print(l)
def prime():
    for i in l:
        if i==2:
            l1.append(i)
        elif i%2==0 or i==1:
            continue
        else:
            f=0
            for j in range(3,isqrt(i)+1,2):
                if i%j==0:
                    f=1
                    break
            if f==0:
                l1.append(i)
    print(l1)
def sum_mean_median(firstname,lastname,regno):
    s=sum(l1)
    s2=int(mean(l1))
    s3=int(median(l1))
    done=firstname+lastname
    print('sum=',s,'mean=',s2 ,'median=',s3)
    print("Doneby=",done,'(',regno,')')
    s=datetime.today().date().ctime()
    print('Timestamp:',s)

if __name__ == '__main__':
    
    l=[]
    l1=[]
    while(True):
        print('Add Range --- 1')
        print('Check Prime --- 2')
        print('Display SMM --- 3')
        print('Exit --- 4')
        print('Enter ur choice : ')
        ch = int(input())
        if ch == 1:
            sr = int(input('Enter start range : '))
            er = int(input('Enter end range : '))
            myrand(sr,er)
        elif ch == 2:
            prime()
        elif ch == 3:
            firstname=input("Enter Firstname:")
            lastname=input("Enter Lastname:")
            regno=int(input("Enter Register No:"))
            sum_mean_median(firstname,lastname,regno)   
        else:
            break

