from datetime import *
def read_data():
    l=[]
    name=input("Enter a Name:")
    dob=input("Enter a Date of brith(dd\mm\yyyy):")
    contact=int(input('Enter a phone no:'))
    email=input('Enter Email.id:')
    l.append(name)
    l.append(dob)
    l.append(contact)
    l.append(email)
    vl.append(l)
def age_eligible():
    s=str(datetime.now().date())
    r=s[0:4:1]
    for i in vl:
        p=str(i[1][6::])
        age=int(r)-int(p)
        if age>=18 and age<45:
            i.append(age)
            el.append(i)
    
def volunteers_list():
     for i in el:
         print(i)
if __name__ == '__main__':
    
    vl=[]
    el=[]
    while(True):
        print('Add data --- 1')
        print('Check Eligiblity --- 2')
        print('Display Eligible --- 3')
        print('Exit --- 4')
        print('Enter ur choice : ')
        ch = int(input())
        if ch == 1:
            read_data()
        elif ch == 2:
            age_eligible()
        elif ch == 3:
            volunteers_list()
        else:
            break


    
