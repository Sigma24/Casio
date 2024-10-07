import  numpy as np
import  math as mp
import  matplotlib.pyplot as plt

def SETUP():
    print()

def MEMORY():
    print()

def all():
    print()


def  Clear():
       print("1:SETUP           2:MEMORY")
       print("3:ALL  ")
       a=int(input(""))
       if a== 1:
             SETUP()
       elif a==2:
               MEMORY()
       elif a==3:
                all()
       else:
               pass






def  Nine_Button(Shift_Key,Alpha_key):
    if  Shift_Key==1:
           Clear()
           Shift_Key=0
    elif Alpha_key==1:
        pass
        Alpha_key=0
    else:
        val=9
        return val

Nine_Button(0,0)
