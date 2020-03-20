import os
import pickle
f2=open("Users.dat","rb")
t=open("temp.dat","wb")
t.close()
f2.close()
os.remove("Users.dat")
os.rename("temp.dat","Users.dat")
