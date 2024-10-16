import  numpy as np
import  math as mp
import  matplotlib.pyplot as plt

import  ShiftKey
import  AlphaKey


def  conversion_Number():
         print()



def  eight_Button():
    if  ShiftKey.shift()==1:
           conversion_Number()

    elif AlphaKey.alpha()==1:
        pass

    else:
        return 8

if __name__ == "__main__":

  eight_Button()
