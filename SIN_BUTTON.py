import numpy as np
import math as mp
import matplotlib.pyplot as plt

import MODES_BUTTON
import  ShiftKey
import  AlphaKey


def sin(input, fix=0):
    if  -mp.inf < input < mp.inf:
        if MODES_BUTTON.get_current_mode() == "DEG":
            conv = np.radians(input)
            result = np.sin(conv)

        elif MODES_BUTTON.get_current_mode()== 'RAD':
            result = np.sin(input)

        elif MODES_BUTTON.get_current_mode() == 'GRAD':
            convo = (input * np.pi / 200)
            result = np.sin(convo)


        else:
            print("Math error")
            return None
        if fix <= 0:
            fix=9
        rounded_result=round(result,fix)
        print(f"sin({input}): {rounded_result}")
        singraph(input,MODES_BUTTON.get_current_mode())
        return result
    else:
        print("Math error")
        return None
def singraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360

    if not -mp.inf<starting<mp.inf and not -mp.inf<ending<mp.inf:
      print("Math error")


    value = np.linspace(starting, ending, 200)
    cal_value = []


    for i in value:
        try:
             if mode == "DEG":
                 conv = np.radians(i)
                 val = np.sin(conv)
                 print(f"The sin of {i} in DEG is {val}")
             elif mode== "RAD":
                 val = np.sin(i)
                 print(f"The sin of {i} in RAD is {val}")
             elif mode == "GRAD":
                 convo = (i * np.pi / 200)
                 val = np.sin(convo)
                 print(f"The sin of {i} in gRAD is {val}")
             else:
                 print("Math error")
                 return None
             cal_value.append(val)
        except ValueError:
             print(f"Skipping the value of {i} duo domain error")
             continue


    plt.plot(value, cal_value, label=f"f(sin(x)) of type {MODES_BUTTON.get_current_mode()}")
    plt.xlabel('x')
    plt.ylabel(f'f(sin(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def arcsin(input,fix=0):
    if -1<=input<=1:
        if MODES_BUTTON.get_current_mode()== "DEG":
            conv = np.radians(input)
            result = np.arcsin(conv)

        elif MODES_BUTTON.get_current_mode() == 'RAD':
            result = np.arcsin(input)
        elif MODES_BUTTON.get_current_mode() == 'GRAD':
            convo = (input * np.pi/200)
            result = np.arcsin(convo)

        else:
            print("Math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"sin⁻¹({input}): {rounded_result}")
        arcsingraph(input,MODES_BUTTON.get_current_mode())
        return result
    else:
        print("Math error")
        return None
def arcsingraph(v,mode):
    print("About to plot a graph")
    if mode == "RAD" or mode == "DEG":
        starting = max(v - 1, -1)
        ending = min(v + 1, 1)
    else:
        starting = max(v - 1, -1)
        ending = min(v + 1, 1)


    if starting < -1 or ending > 1:
        print("Math error: Starting and ending points must be within the range [-1, 1].")
        return

    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode== "DEG":
                conv = np.radians(i)
                val = np.arcsin(np.sin(conv))
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The sin⁻¹ of {i} in DEG is {val}")

            elif mode== "RAD":
                val = np.arcsin(i)
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The sin⁻¹ of {i} in RAD is {val}")

            elif mode== "GRAD":

                convo = (i * np.pi / 200)
                val = np.arcsin(np.sin(convo))
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The sin⁻¹ of {i} in GRAD is {val}")

            else:
                print("Math error: Invalid mode.")
                return

            cal_value.append(val)
        except ValueError:
            print(f"Skipping value {i} due to error.")
            continue

    plt.plot(value, cal_value, label=f"f(sin⁻¹(x)) of type {MODES_BUTTON.get_current_mode()}")
    plt.xlabel('x')
    plt.ylabel(f'f(sin⁻¹(x))')
    plt.grid(True)
    plt.legend()
    plt.show()




# ACTUAL CALL  "def sin_Button(Shift_key,value,mode,fix_key)"
def sin_Button(fix_key):
    if AlphaKey.alpha()==1:

        return 'D'

    if ShiftKey.shift() == 1:
        value = float(input("Enter a value for sin⁻¹(x): "))
        type = input("Enter a type:")
        fix=0
        if fix_key==1:
           while True:
              try:
                  fix = int(input("1-9: "))
                  if 0 <= fix <= 9:
                      break

              except ValueError:
                    print("")



        arcsin(value,fix)
        Shift_key=0
    else:
        value = float(input("Enter a value for sin(x): "))
        type = input("Enter a type: ")
        fix=0
        if fix_key==1:
           while True:
              try:
                  fix = int(input("1-9: "))
                  if 1 <= fix <= 9:
                      break
              except ValueError:
                    print("")
        sin(value,fix)

if __name__ == "__main__":
    sin_Button(0,)