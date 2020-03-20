import os
import pickle
import re
amt=100000
class user:
    def __init__(self,fname,lname,uname,pnum,cardno,pi,bal):
        self.f_name=fname
        self.l_name=lname
        self.u_name=uname
        self.p_number=pnum
        self.card_no=cardno
        self.pin=pi
        self.balance=bal
    def display(self):
        print ("Balance: ",self.balance)
        print ("".center(104,"-"))
    def display_d(self):
        print ("First name: ",self.f_name)
        print ("Last name: ",self.l_name)
        print ("Phone number: ",self.p_number)
        print ("".center(104,"-"))
def unique_uname(u):
    f=open("Users.dat","rb")
    flag=0
    try:
        while True:
            x=pickle.load(f)
            if (x.u_name==u):
                flag=1
                f.close()
                return (False)
    except EOFError:
        pass
    if (flag==0):
        f.close()
        return (True)
def unique_phone(p):
    f=open("Users.dat","rb")
    flag=0
    try:
        while True:
            x=pickle.load(f)
            if (x.p_number==p):
                flag=1
                f.close()
                return (False)
    except EOFError:
        pass
    if (flag==0):
        f.close()
        return (True) 
def create_account():
    pattu="^\w+$"
    global cnum,amt
    flagp,flagu=0,0
    f=open("Users.dat","ab")
    while True:
        fname=input("Enter First Name ")
        if (fname.isalpha()==False):
            print ("First name can constitute of only alphabets")
        else:
            break
    while True:
        lname=input("Enter Last Name ")
        if (lname.isalpha()==False):
            print ("Last name can constitute of only alphabets")
        else:
            break
    print ("Length of username must be between 8-17 characters")
    print ("Username can contain alphabets, digits and the special character _")
    while True:
        while True:
            uname=input("Enter Username ")
            if (8<=len(uname)<=17):
                if (re.match(pattu,uname)):
                    break
                else:
                    print ("Username can contain alphabets, digits and the special character _")
            else:
                print ("Length of username must be between 8-17 characters")
        if (unique_uname(uname)==False):
            print ("Username already used")
            print ("To sign in, press 1, to enter another username, press 2")
            while True:
                try: 
                    ch1=int(input("Enter choice "))
                    break
                except ValueError:
                    print ("Choice should be a digit")
            if (ch1==1):
                print ("".center(104,"-"))
                login()
                break
            elif (ch1==2):
                pass
            else:
                print("Enter Choice correctly")
        else:
            flagu=1
            break
    while True:
        while True:
            while True:
                try: 
                    pnum=int(input("Enter User Phone Number "))
                    break
                except ValueError:
                    print ("Phone number should consist of only digits")
            if (len(str(pnum))==10):
                break
            else:
                print ("Invalid phone number")
        if (unique_phone(pnum)==False):
            print ("Phone number already registered")
            print ("To sign in, press 1, to enter another number, press 2")
            while True:
                try: 
                    ch1=int(input("Enter choice "))
                    break
                except ValueError:
                    print ("Choice should be a digit")
            if (ch1==1):
                print ("".center(104,"-"))
                login()
                break
            elif (ch1==2):
                pass
            else:
                print("Enter Choice correctly")
        else:
            flagp=1
            break
    if (flagp==1 and flagu==1):
        while True:
            while True:
                try: 
                    pin=int(input("Enter pin "))
                    break
                except ValueError:
                    print ("Pin should consist of only digits")
            if (len(str(pin))==4):
                break
            else:
                print ("Pin should be of 4 digits")
        f2=open("card_number.txt","r")
        t=open("temp.txt","w")
        while True:
            s=f2.readline()
            if not s:
                break
            c_num=int(s)
            t.write(str(c_num+1))
        print ("Your card number is ",c_num)
        t.close()
        f2.close()
        os.remove("card_number.txt")
        os.rename("temp.txt","card_number.txt")
        obj=user(fname,lname,uname,pnum,c_num,pin,amt)
        pickle.dump(obj,f)
        f.close()
        print("Account has been sucessfully created")
        print ("".center(104,"-"))
def withdraw_cash(x):
    while True:
        try:
            amt=int(input("Enter Amount to be withdrawn "))
            break
        except ValueError:
            print ("Amount should consist of only digits")
    if (x.balance<amt):
        print ("Insufficient funds! ")
        login_settings(x)
    else:
        f=open("Users.dat","rb")
        t=open("temp.dat","wb")
        try:
            while True:
                y=pickle.load(f)
                if (y.u_name==x.u_name):
                    obj=user(x.f_name,x.l_name,x.u_name,x.p_number,x.card_no,x.pin,x.balance-amt)
                    pickle.dump(obj,t)
                else:
                    pickle.dump(y,t)
        except EOFError:
            pass
        t.close()
        f.close()
        os.remove("Users.dat")
        os.rename("temp.dat","Users.dat")
        print (amt, " has been withdrawn from your account")
        print ("".center(104,"-"))
        login_settings(obj)
def change_phone_number(x):
    while True:
        while True:
            while True:
                try: 
                    pnum=int(input("Enter User Phone Number "))
                    break
                except ValueError:
                    print ("Phone number should consist of only digits")
            if (len(str(pnum))==10):
                break
            else:
                print ("Invalid phone number")
        if (unique_phone(pnum)==False):
            print ("Phone number already registered")
        else:
            break
    f=open("Users.dat","rb")
    t=open("temp.dat","wb")
    try:
        while True:
            y=pickle.load(f)
            if (y.u_name==x.u_name):
                obj=user(x.f_name,x.l_name,x.u_name,pnum,x.card_no,x.pin,x.balance)
                pickle.dump(obj,t)
            else:
                pickle.dump(y,t)
    except EOFError:
        pass
    t.close()
    f.close()
    os.remove("Users.dat")
    os.rename("temp.dat","Users.dat")
    print ("Your phone number has successfully been changed to ",pnum)
    print ("".center(104,"-"))
    login_settings(obj)
def add_funds(x):
    while True:
        try:
            amt=int(input("Enter Amount to be withdrawn "))
            break
        except ValueError:
            print ("Amount should consist of only digits")
    f=open("Users.dat","rb")
    t=open("temp.dat","wb")
    try:
        while True:
            y=pickle.load(f)
            if (y.u_name==x.u_name):
                obj=user(x.f_name,x.l_name,x.u_name,x.p_number,x.card_no,x.pin,x.balance+amt)
                pickle.dump(obj,t)
            else:
                pickle.dump(y,t)
    except EOFError:
        pass
    t.close()
    f.close()
    os.remove("Users.dat")
    os.rename("temp.dat","Users.dat")
    print (amt, "has been successfully added to your account!")
    print ("".center(104,"-"))
    login_settings(obj)
def login_settings(x):
    while True:
        print ("Press 1 to display balance")
        print ("Press 2 to display other details")
        print ("Press 3 to withdraw cash")
        print ("Press 4 to change phone number")
        print ("Press 5 to add funds")
        print ("Press 6 to log out")
        while True:
            try: 
                ch=int(input("Enter choice "))
                break
            except ValueError:
                print ("Choice should be a digit")
        if (ch==1):
            print ("".center(104,"-"))
            x.display()
        elif (ch==2):
            print ("".center(104,"-"))
            x.display_d()
        elif (ch==3):
            print ("".center(104,"-"))
            withdraw_cash(x)
            break
        elif (ch==4):
            print ("".center(104,"-"))
            change_phone_number(x)
            break
        elif (ch==5):
            print ("".center(104,"-"))
            add_funds(x)
            break
        elif (ch==6):
            print ("".center(104,"-"))
            break
        else:
            print ("Please enter choice correctly")
            print ("".center(104,"-"))
def login():
    flag0=0
    flag1=0
    un=input("Enter username")
    f=open("Users.dat","rb")
    try:
        while True:
            x=pickle.load(f)
            if (x.u_name==un):
                flag0=1
                while True:
                    try: 
                        p=int(input("Enter pin "))
                        break
                    except ValueError:
                        print ("Pin should consist only of digits")
                if (p==x.pin):
                    print("Login successful")
                    print ("".center(104,"-"))
                    f.close()
                    login_settings(x)
                    break
                else:
                    print ("Incorrect pin. Transaction denied")
                    flag1=1
                    break
            if (flag1==1):
                break
    except EOFError:
        pass
    if (flag0==0):
        print ("User not found")
        f.close()
#def main():        
print ("Welcome to Axis bank! ".center(107,"-"))
while True:
    print ("Press 1 to create account")
    print ("Press 2 to login")
    print ("Press 3 to exit")
    while True:
        try: 
            ch2=int(input("Enter choice "))
            break
        except ValueError:
            print ("Choice should be a digit")
    if (ch2==1):
        print ("".center(104,"-"))
        create_account()
    elif (ch2==2):
        print ("".center(104,"-"))
        login()
    elif (ch2==3):
        print("Thank You! ".center(106,"-"))
        break
    else:
        print ("Please enter correct choice")
        print ("".center(107,"-"))  

# if __name__=='__main__':
#           main()
    
    
