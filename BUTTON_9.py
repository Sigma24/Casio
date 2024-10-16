import  numpy as np
import  math as mp
import  matplotlib.pyplot as plt
import  ShiftKey
import  AlphaKey

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






def  Nine_Button():
    if  ShiftKey.shift()==1:
           Clear()

    elif AlphaKey.alpha()==1:
        pass

    else:
        return 9

if __name__ == "__main__":

  Nine_Button()
