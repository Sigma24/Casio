import numpy as np
import math as mp
import matplotlib.pyplot as plt

import  MODES_BUTTON
import  ShiftKey
import  AlphaKey



def tan(Value, fix=0):
    if not np.isclose(np.cos(Value),0):
        if MODES_BUTTON.get_current_mode()== "RAD":
            result = np.tan(Value)

        elif MODES_BUTTON.get_current_mode() == "DEG":
            conv_DEG = np.deg2rad(Value)
            result = np.tan(conv_DEG)

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            conv_radian = Value * np.pi / 200
            result = np.tan(conv_radian)

        else:
            print("Math Error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"tan({Value}): {rounded_result}")
        tangraph(Value,MODES_BUTTON.get_current_mode())
        return result
    else:
        print("Math Error")
        return None
def tangraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if np.isclose(np.cos(starting),0) or np.isclose(np.cos(ending),0):
        print("Math error: Value out of domain where cos = 0")
    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
             if mode == "DEG":
                 conv = np.radians(i)
                 val = np.tan(conv)
                 print(f"The tan of {i} in DEG is {val}")
             elif mode == "RAD":
                 val = np.tan(i)
                 print(f"The tan of {i} in RAD is {val}")
             elif mode  == "GRAD":
                 convo = (i * np.pi / 200)
                 val = np.tan(convo)
                 print(f"The tan of {i} in gRAD is {val}")
             else:
                 print("Math error")
                 return None
             cal_value.append(val)
        except ValueError:
              print(f"Skipping the value of {i} duo domain error")
              continue


    plt.plot(value, cal_value, label=f"f(tan(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(tan(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def arctan(input,fix=0):
    if -mp.inf<input<mp.inf:
        if MODES_BUTTON.get_current_mode() == "DEG":
            conv = np.radians(input)
            result = np.arctan(conv)

        elif MODES_BUTTON.get_current_mode() == 'RAD':
            result = np.arctan(input)

        elif MODES_BUTTON.get_current_mode()== 'GRAD':
            convo = (input * np.pi/200)
            result = np.arctan(convo)


        else:
            print("Math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"tan⁻¹({input}): {rounded_result}")
        arctangraph(input,MODES_BUTTON.get_current_mode())
        return result
    else:
        print("Math error")
        return None

def arctangraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if not -mp.inf < starting < mp.inf and not -mp.inf<ending<mp.inf:
        print("Math error: Value out of domain")
    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
       try:
           if mode== "DEG":
               conv = np.radians(i)
               val = np.arctan(conv)
               print(f"the tan⁻¹ of {i} in {mode} is {val}")
           elif mode == "RAD":
               val = np.arctan(i)
               print(f"the tan⁻¹ of {i} in {mode} is {val}")
           elif mode == "GRAD":
               convo = (i * np.pi / 200)
               val = np.arctan(convo)
               print(f"the tan⁻¹ of {i} in {mode} is {val}")
           else:
               print("Math error")
               return None
           cal_value.append(val)
       except ValueError:
           print(f"Skipping the value of {i} due to domain error")
           continue


    plt.plot(value, cal_value, label=f"f(tan⁻¹(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(tan⁻¹(x))')
    plt.grid(True)
    plt.legend()
    plt.show()

# ACTUAL CALL  "def tan_Button(Shift_key,value,mode,fix_key)"
def Tan_Button(fix_key):
    if AlphaKey.alpha() == 1:

        return 'F'

    if ShiftKey.shift() == 1:
        value = float(input("Enter a value for cos⁻¹(x): "))
        type = input("Enter a type: ")
        fix = 0
        if fix_key == 1:
            while True:
                try:
                    fix = int(input("1-9: "))
                    if 1 <= fix <= 9:
                        break
                except ValueError:
                    print("")
        arctan(value,fix)
        Shift_key=0
    else:
        value = float(input("Enter a value for cos(x): "))
        type = input("Enter a type: ")
        fix = 0
        if fix_key == 1:
            while True:
                try:
                    fix = int(input("1-9: "))
                    if 1 <= fix <= 9:
                        break
                except ValueError:
                    print("")
        tan(value,fix)


if __name__ == "__main__":
    Tan_Button(1)