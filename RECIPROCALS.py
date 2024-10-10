import numpy as np
import math as mp
import matplotlib.pyplot as plt

import MODES_BUTTON


def cosec(value, fix=0):
    if not np.isclose(np.sin(value), 0):
        if MODES_BUTTON.get_current_mode()  == "DEG":
            val = np.deg2rad(value)
            result = 1 / np.sin(value)


        if MODES_BUTTON.get_current_mode()  == "RAD":
            result = 1 / np.sin(value)

        elif MODES_BUTTON.get_current_mode()  == "GRAD":
            val = value * np.pi / 200
            result = 1 / np.sin(value)

        else:
            print("Math error")
            return None
        if fix <= 0:
            fix=10
        rounded_result=round(result,fix)
        print(f"cosec({value}): {rounded_result}")
        cosecgraph(value,MODES_BUTTON.get_current_mode() )
        return result
    else:
        print("Math error")
        return None

def cosecgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if  np.isclose(np.sin(starting), 0) or  np.isclose(np.sin(ending), 0):
        print("Math error: Value out of domain where sin is 0")
    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
              if mode == "DEG":
                  conv = np.radians(i)
                  val = 1/np.sin(conv)
                  print(f"the cosec of {i} in {mode} is {val}")
              elif mode == "RAD":
                  val = 1/np.sin(i)
                  print(f"the cosec of {i} in {mode} is {val}")
              elif mode == "GRAD":
                  convo = (i * np.pi / 200)
                  val = 1/np.sin(convo)
                  print(f"the cosec of {i} in {mode} is {val}")
              else:
                  print("Math error")
                  return None

              cal_value.append(val)
        except ValueError:
                 print(f"Skipping the value {i} due to domain error")
                 continue
    plt.plot(value, cal_value, label=f"f(cosec(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel('f(cosec(x))')

    plt.grid(True)
    plt.legend()
    plt.show()




def sec(value,  fix=0):
    if not np.isclose(np.cos(value), 0):
        if MODES_BUTTON.get_current_mode()  == "DEG":
            val = np.deg2rad(value)
            result = 1 / np.cos(value)


        if MODES_BUTTON.get_current_mode()  == "RAD":
            result = 1 / np.cos(value)

        elif MODES_BUTTON.get_current_mode()  == "GRAD":
            val = value * np.pi / 200
            result = 1 / np.cos(value)

        else:
            print("Math error")
            return None
        if fix <= 0:
            fix=10
        rounded_result=round(result,fix)
        print(f"sec({value}): {rounded_result}")
        secgraph(value,MODES_BUTTON.get_current_mode() )
        return result
    else:
        print("Math error")
        return None

def secgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if  np.isclose(np.cos(starting), 0) or  np.isclose(np.cos(ending), 0):
        print("Math error: Value out of domain where cos is 0")

    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = 1/np.cos(conv)
                print(f"the sec of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = 1/np.cos(i)
                print(f"the sec of {i} in {mode} is {val}")
            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = 1/np.cos(convo)
                print(f"the  sec of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
                 print(f"Skipping the value {i} due to domain error")
                 continue
    plt.plot(value, cal_value, label=f"f(sec(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel('f(sec(x))')
    plt.grid(True)
    plt.legend()
    plt.show()




def cot(value,  fix=0):
    if not np.isclose(np.tan(value), 0):
        if MODES_BUTTON.get_current_mode() == "DEG":
            val = np.deg2rad(value)
            result = 1 / np.tan(value)


        if MODES_BUTTON.get_current_mode() == "RAD":
            result = 1 / np.tan(value)

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            val = value * np.pi / 200
            result = 1 / np.tan(value)

        else:
            print("Math error")
            return None
        if fix <= 0:
            fix=10
        rounded_result=round(result,fix)
        print(f"cot({value}): {rounded_result}")
        cotgraph(value,MODES_BUTTON.get_current_mode())
        return result
    else:
        print("Math error")
        return None

def cotgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if  np.isclose(np.tan(starting), 0) or  np.isclose(np.tan(ending), 0):
        print("Math error: Value out of domain where tan is 0")

    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = 1/np.tan(conv)
                print(f"the tan_inverse of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = 1/np.tan(i)
                print(f"the tan_inverse of {i} in {mode} is {val}")
            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = 1/np.tan(convo)
                print(f"the tan_inverse of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
                print(f"Skipping the value {i} due to domain error")
                continue
    plt.plot(value, cal_value, label=f"f(cot(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel('f(cot(x))')
    plt.grid(True)
    plt.legend()
    plt.show()







def arccosec(value,fix=0):
    if np.abs(value)>=1:
        if MODES_BUTTON.get_current_mode()=="DEG":
            val=np.deg2rad(value)
            vala=np.arcsin(1/(val))

        elif MODES_BUTTON.get_current_mode() == "RAD":
            vala = np.arcsin(1/(value))

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            val = value * np.pi/200
            vala = np.arcsin(1/val)
        else:
            print("Math error")
            return None
        if fix <= 0:
            fix=10
        rounded_result=round(vala,fix)
        print(f"cosec⁻¹({value}): {rounded_result}")
        arccosecgraph(value,MODES_BUTTON.get_current_mode())
        return vala
    else:
        print("Math error")
        return None

def arccosecgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360


    if starting == 0 or ending == 0:
        print("Math error: Value out of domain.")
        return

    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = np.arcsin(1 / conv)
                if np.isnan(val):
                    print(f"Skipping value {i} due to invalid arccosine.")
                    continue
                print(f"the cosec⁻¹ of {i} in {mode} is {val}")

            elif mode == "RAD":
                val = np.arcsin(1 / i)
                if np.isnan(val):
                    print(f"Skipping value {i} due to invalid arccosine.")
                    continue
                print(f"the cosec⁻¹ of {i} in {mode} is {val}")
            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.arcsin(1 / convo)
                if np.isnan(val):
                    print(f"Skipping value {i} due to invalid arccosine.")
                    continue
                print(f"the cosec⁻¹ of {i} in {mode} is {val}")
            else:
                print("Math error: Invalid mode.")
                return None

            cal_value.append(val)
        except ValueError:
            print(f"Skipping value {i} due to ValueError.")
            continue

    plt.plot(value, cal_value, label=f"f(arccosec(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(arccosec(x))')
    plt.grid(True)
    plt.legend()
    plt.show()








def arcsec(value, fix=0):
    if np.abs(value)>=1:
        if MODES_BUTTON.get_current_mode()=="DEG":
            val=np.deg2rad(value)
            vala=np.arccos(1/(value))

        elif MODES_BUTTON.get_current_mode() == "RAD":
            vala = np.arccos(1/(value))

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            val = value * np.pi/200
            vala = np.arccos(1/value)

        else:
            print("Math error")
            return None
        if fix <= 0:
            fix=10
        rounded_result=round(vala,fix)
        print(f"sec⁻¹({value}): {rounded_result}")
        arcsecgraph(value,MODES_BUTTON.get_current_mode())
        return vala
    else:
        print("Math error")
        return None


def arcsecgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360

    if starting == 0 or ending == 0:
        print("Math error: Value out of domain.")
        return

    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = np.arccos(1 / conv)
                if np.isnan(val):
                    print(f"Skipping value {i} due to invalid arccosine.")
                    continue
                print(f"the sec⁻¹ of {i} in {mode} is {val}")

            elif mode == "RAD":
                val = np.arccos(1 / i)
                if np.isnan(val):
                    print(f"Skipping value {i} due to invalid arccosine.")
                    continue
                print(f"the sec⁻¹ of {i} in {mode} is {val}")

            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.arccos(1 / convo)
                if np.isnan(val):
                    print(f"Skipping value {i} due to invalid arccosine.")
                    continue
                print(f"the sec⁻¹ of {i} in {mode} is {val}")

            else:
                print("Math error: Invalid mode.")
                return None

            cal_value.append(val)
        except ValueError:
            print(f"Skipping value {i} due to ValueError.")
            continue

    plt.plot(value, cal_value, label=f"f(arcsec(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(arcsec(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def arccot(value,fix=0):
    if -mp.inf<value<mp.inf:
        if MODES_BUTTON.get_current_mode()=="DEG":
            val=np.deg2rad(value)
            vala=np.arctan(1/(value))

        elif MODES_BUTTON.get_current_mode() == "RAD":
            vala = np.arctan(1/(value))

        elif MODES_BUTTON.get_current_mode()== "GRAD":
            val = value * np.pi/200
            vala = np.arctan(1/value)

        else:
            print("Math error")
            return None
        if fix <= 0:
            fix=10
        rounded_result=round(vala,fix)
        print(f"cot⁻¹({value}): {rounded_result}")
        arccotgraph(value,MODES_BUTTON.get_current_mode())
        return vala
    else:
        print("Math error")
        return None

def arccotgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode== "RAD" else v + 360
    if not -mp.inf < starting< mp.inf and not -mp.inf<ending<mp.inf:
        print("Math error: Value out of domain")
    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = np.arctan(1 / (conv))
                print(f"the cot⁻¹ of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = np.arctan(1 / (i))
                print(f"the cot⁻¹ of {i} in {mode} is {val}")

            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.arctan(1 / (convo))
                print(f"the cot⁻¹ of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
                   print(f"Skipping the value {i} due to domain error")
                   continue
    plt.plot(value, cal_value, label=f"f(arccot(x)) of type {mode.capitalize()}")
    plt.xlabel('x')
    plt.ylabel(f'f(arccot(x))')
    plt.grid(True)
    plt.legend()
    plt.show()







value=float(input("Enter a value"))
Type=input("Enter a type")
if __name__ == "__main__":
    arccot(value,1)





















