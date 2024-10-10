import numpy as np
import math as mp
import matplotlib.pyplot as plt
import  MODES_BUTTON
import  ShiftKey
import  AlphaKey


def cos(input,fix=0):
    if -mp.inf<input<mp.inf:
        if MODES_BUTTON.get_current_mode() == "DEG":
            conv = np.radians(input)
            result=np.cos(conv)

        elif MODES_BUTTON.get_current_mode()  == "RAD":
            result = np.cos(input)

        elif MODES_BUTTON.get_current_mode()  == "GRAD":
            convo = (input * np.pi/200)
            result=np.cos(convo)


        else:
            print("Math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"cos({input}): {rounded_result}")
        cosgraph(input,MODES_BUTTON.get_current_mode() )
        return result
    else:
        print("Math error")
        return None

def cosgraph(v,mode):
    print("About to plot a graph")
    starting=v
    ending=v+2*np.pi if mode  == "RAD" else v+360
    if not -mp.inf < starting < mp.inf or not -mp.inf < ending < mp.inf:
        print("Math error")
    value= np.linspace(starting,ending,200)
    cal_value = []

    for i in value:
        try:
            if mode  == "DEG":
                conv = np.radians(i)
                val = np.cos(conv)
                print(f"The cos of {i} in degree is {val}")
            elif mode  == "RAD":
                val = np.cos(i)
                print(f"The cos of {i} in radian is {val}")
            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.cos(convo)
                print(f"The cos of {i} in gradian is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
              print(f"Skipping the value of {i} duo domain error")
              continue


    plt.plot(value, cal_value, label=f"f(cos(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(cos(x))')
    plt.grid(True)
    plt.legend()
    plt.show()




def arccos(input,fix=0):
    if -1<=input<=1:
        if MODES_BUTTON.get_current_mode()  == "DEG":
            conv = np.radians(input)
            result = np.arccos(conv)

        elif MODES_BUTTON.get_current_mode()  == 'RAD':
            result = np.arccos(input)

        elif MODES_BUTTON.get_current_mode()  == 'GRAD':
            convo = (input * np.pi/200)
            result = np.arccos(convo)


        else:
            print("Math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"cos⁻¹({input}): {rounded_result}")

        arccosgraph(input,MODES_BUTTON.get_current_mode() )
        return result
    else:
        print("Math error")
        return None

def arccosgraph(v,mode):
    print("About to plot a graph")

    if mode == "radian" or mode == "degree":
        starting = max(v - 1, -1)
        ending = min(v + 1, 1)
    else:
        starting = max(v - 1, -1)
        ending = min(v + 1, 1)
    if (starting < -1 or starting > 1) or (ending < -1 or ending > 1):
        print("Math error: Value out of domain.")
        return

    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "degree":
                conv = np.radians(i)
                val = np.arccos(np.cos(conv))
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The cos⁻¹ of {i} in degree is {val}")

            elif mode == "radian":
                val = np.arccos(i)
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The cos⁻¹ of {i} in radian is {val}")

            elif mode == "gradian":

                convo = (i * np.pi / 200)
                val = np.arccos(np.cos(convo))
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The cos⁻¹ of {i} in gradian is {val}")

            else:
                print("Math error: Invalid mode.")
                return

            cal_value.append(val)
        except ValueError:
            print(f"Skipping value {i} due to error.")
            continue

    plt.plot(value, cal_value, label=f"f(cos⁻¹(x)) of type {mode }")
    plt.xlabel('x')
    plt.ylabel(f'f(cos⁻¹(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


# ACTUAL CALL  "def cos_Button(Shift_key,value,mode,fix_key)"
def cos_Button(fix_key):
    if AlphaKey.alpha()==1:
        return 'E'


    if ShiftKey.shift()== 1:
        value = float(input("Enter a value for cos⁻¹(x): "))
        type = input("Enter a type: ")
        fix=0
        if fix_key == 1:
            while True:
                try:
                    fix = int(input("1-9: "))
                    if 1 <= fix <= 9:
                        break
                except ValueError:
                    print("")
        arccos(value,fix)

    else:
        value = float(input("Enter a value for cos(x): "))
        type = input("Enter a type: ")
        fix=0
        if fix_key == 1:
            while True:
                try:
                    fix = int(input("1-9: "))
                    if 1 <= fix <= 9:
                        break
                except ValueError:
                    print("")
        cos(value,fix)



if __name__ == "__main__":
    cos_Button(1)

