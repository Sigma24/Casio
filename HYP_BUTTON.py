import numpy as np
import math as mp
import matplotlib.pyplot as plt
import  MODES_BUTTON
import  ShiftKey
import  AlphaKey



def cosh(Value, fix=0):
    if -mp.inf < Value < mp.inf:
        if MODES_BUTTON.get_current_mode() == "DEG":
            deg_value = np.deg2rad(Value)
            result = np.cosh(deg_value)


        elif  MODES_BUTTON.get_current_mode() == "RAD":
            result = np.cosh(Value)

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            con = Value * np.pi / 200
            result = np.cosh(con)

        else:
            print("math error")
            return None
        if fix <= 0:
            fix = 9
        rounded_result = round(result, fix)
        print(f"cosh({Value}): {rounded_result}")
        coshgraph(Value,MODES_BUTTON.get_current_mode())
        return result


    else:
        print("math error")
        return None


def coshgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if not -mp.inf < starting < mp.inf or not -mp.inf < ending < mp.inf:
        print("Math error: Value out of domain")
    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = np.cosh(conv)
                print(f"the cosh of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = np.cosh(i)
                print(f"the cosh of {i} in {mode} is {val}")

            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.cosh(convo)
                print(f"the cosh of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
            print(f"Skipping the value {i} due to domain error")
            continue

    plt.plot(value, cal_value, label=f"f(cosh(x)) of type {MODES_BUTTON.get_current_mode()}")
    plt.xlabel('x')
    plt.ylabel(f'f(cosh(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def sinh(Value, fix=0):
    if -mp.inf < Value < mp.inf:
        if MODES_BUTTON.get_current_mode() == "DEG":
            deg_value = np.deg2rad(Value)
            result = np.sinh(deg_value)


        elif MODES_BUTTON.get_current_mode()== "RAD":
            result = np.sinh(Value)

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            con = Value * np.pi / 200
            result = np.sinh(con)

        else:
            print("math error")
            return None
        if fix <= 0:
            fix = 9
        rounded_result = round(result, fix)
        print(f"sinh({Value}): {rounded_result}")
        sinhgraph(Value,MODES_BUTTON.get_current_mode())
        return result


    else:
        print("math error")
        return None


def sinhgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360

    value = np.linspace(starting, ending, 200)
    cal_value = []
    if not -mp.inf < starting < mp.inf and not -mp.inf < ending < mp.inf:
        print("Math error: Value out of domain")
    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = np.sinh(conv)
                print(f"the sinh of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = np.sinh(i)
                print(f"the sinh of {i} in {mode} is {val}")

            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.sinh(convo)
                print(f"the sinh of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
            print(f"Skipping the value {i} due to domain error")
            continue

    plt.plot(value, cal_value, label=f"f(sinh(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(sinh(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def tanh(Value, fix=0):
    if -mp.inf < Value < mp.inf:
        if MODES_BUTTON.get_current_mode() == "DEG":
            deg_value = np.deg2rad(Value)
            result = np.tanh(deg_value)


        elif MODES_BUTTON.get_current_mode() == "RAD":
            result = np.tanh(Value)

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            con = Value * np.pi / 200
            result = np.tanh(con)

        else:
            print("math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"tan({Value}): {rounded_result}")
        tanhgraph(Value,MODES_BUTTON.get_current_mode())
        return result


    else:
        print("math error")
        return None


def tanhgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if not -mp.inf < starting < mp.inf and not -mp.inf < ending < mp.inf:
        print("Math error: Value out of domain")
    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = np.tanh(conv)
                print(f"the tanh of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = np.tanh(i)
                print(f"the tanh of {i} in {mode} is {val}")
            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.tanh(convo)
                print(f"the tanh of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
            print(f"Skipping the value {i} due to domain error")
            continue

    plt.plot(value, cal_value, label=f"f(tanh(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(tanh(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def arcsinh(Value, fix=0):
    if -1 <= Value <= 1:
        if MODES_BUTTON.get_current_mode()== "DEG":
            deg_value = np.deg2rad(Value)
            result = np.arcsinh(deg_value)


        elif MODES_BUTTON.get_current_mode() == "RAD":
            result = np.arcsinh(Value)

        elif MODES_BUTTON.get_current_mode() == "GRAD":
            con = Value * np.pi / 200
            result = np.arcsinh(con)

        else:
            print("math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"sinh⁻¹({Value}): {rounded_result}")
        arcsinhgraph(Value,MODES_BUTTON.get_current_mode())
        return result


    else:
        print("math error")
        return None


def arcsinhgraph(v,mode):
    print("About to plot a graph")
    if mode == "RAD" or mode == "DEG":
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
            if mode == "DEG":
                conv = np.radians(i)
                val = np.arcsinh(conv)
                print(f"the sinh⁻¹ of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = np.arcsinh(i)
                print(f"the sinh⁻¹ of {i} in {mode} is {val}")

            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.arcsinh(convo)
                print(f"the sinh⁻¹ of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
            print(f"Skipping the value {i} due to domain error")
            continue

    plt.plot(value, cal_value, label=f"f(sinh⁻¹(x)) of type {mode}")
    plt.xlabel('x')
    plt.ylabel(f'f(sinh⁻¹(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def arccosh(Value, fix=0):
    if 1 < Value <= mp.inf:
        if MODES_BUTTON.get_current_mode() == "DEG":
            deg_value = np.deg2rad(Value)
            result = np.arccosh(deg_value)


        elif MODES_BUTTON.get_current_mode() == "RAD":
            result = np.arccosh(Value)

        elif MODES_BUTTON.get_current_mode()== "GRAD":
            con = Value * np.pi / 200
            result = np.arccosh(con)

        else:
            print("math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"cosh⁻¹({Value}): {rounded_result}")
        arccoshgraph(Value,MODES_BUTTON.get_current_mode())
        return result


    else:
        print("math error")
        return None


def arccoshgraph(v,mode):
    print("About to plot a graph")
    starting = v
    ending = v + 2 * np.pi if mode == "RAD" else v + 360
    if starting <= 1 or ending <= 1:
        print("Math error: Value Out of domain")
        return
    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "DEG":
                conv = np.radians(i)
                val = np.arccosh(conv)
                print(f"the cosh⁻¹ of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = np.arccosh(i)
                print(f"the cosh⁻¹ of {i} in {mode} is {val}")
            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.arccosh(convo)
                print(f"the cosh⁻¹ of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None
            cal_value.append(val)
        except ValueError:
            print("Skipping value of {i} due to domain error")
            continue

    plt.plot(value, cal_value, label=f"f(cosh⁻¹(x)) of type {mode.capitalize()}")
    plt.xlabel('x')
    plt.ylabel(f'f(cosh⁻¹(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


def arctanh(Value, fix=0):
    if -1 <= Value <= 1:
        if MODES_BUTTON.get_current_mode()== "DEG":
            deg_value = np.deg2rad(Value)
            result = np.arctanh(deg_value)


        elif MODES_BUTTON.get_current_mode()== "RAD":
            result = np.arctanh(Value)
        elif MODES_BUTTON.get_current_mode() == "GRAD":
            con = Value * np.pi / 200
            result = np.arctanh(con)

        else:
            print("math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"tanh⁻¹({Value}): {rounded_result}")
        arctanhgraph(Value,MODES_BUTTON.get_current_mode())
        return result


    else:
        print("math error")
        return None


def arctanhgraph(v,mode):
    print("About to plot a graph")
    if mode == "RAD" or mode == "DEG":
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
            if mode == "DEG":
                conv = np.radians(i)
                val = np.arctanh(conv)
                print(f"the tanh⁻¹ of {i} in {mode} is {val}")
            elif mode == "RAD":
                val = np.arctanh(i)
                print(f"the tanh⁻¹ of {i} in {mode} is {val}")
            elif mode == "GRAD":
                convo = (i * np.pi / 200)
                val = np.arctanh(convo)
                print(f"the tanh⁻¹ of {i} in {mode} is {val}")
            else:
                print("Math error")
                return None
            cal_value.append(val)
        except ValueError:
            print(f"Skipping the value {i} due to domain error")
            continue

    plt.plot(value, cal_value, label=f"f(tanh⁻¹(x)) of type {mode.capitalize()}")
    plt.xlabel('x')
    plt.ylabel(f'f(tanh⁻¹(x))')
    plt.grid(True)
    plt.legend()
    plt.show()

def ABS(input):
      return np.abs(input)



def Hype_button(Alpha_key,fix_key,Shift_key):
    if AlphaKey.alpha()==1:
        return"C"
    elif ShiftKey.shift()==1:
         val =float(input("Enter Value"))
         return ABS(val)



    else:
        print("1:sinh           2:sinh⁻¹")
        print("3:cosh           4:cosh⁻¹")
        print("4:tanh           5:tanh⁻¹")
        users_input = int(input())

        if users_input == 1:
            value = float(input("enter a value at sinh"))
            type = input("enter a type")
            fix = 0
            if fix_key == 1:
                while True:
                    try:
                        fix = int(input("1-9:"))
                        if 1 <= fix <= 9:
                            break
                    except ValueError:
                        print("")
            sinh(value, fix)

        elif users_input == 2:
            value = float(input("enter a value sinh⁻¹ "))
            type = input("enter a type")
            fix = 0
            if fix_key == 1:
                while True:
                    try:
                        fix = int(input("1-9: "))
                        if 1 <= fix <= 9:
                            break
                    except ValueError:
                        print("")
            arcsinh(value, fix)

        elif users_input == 3:
            value = float(input("enter a value cosh"))
            type = input("enter a type")

            fix = 0
            if fix_key == 1:
                while True:
                    try:
                        fix = int(input("1-9: "))
                        if 1 <= fix <= 9:
                            break
                    except ValueError:
                        print("")
            cosh(value,fix )
        elif users_input == 4:
            value = float(input("enter a value cosh⁻¹"))
            type = input("enter a type")
            fix = 0
            if fix_key == 1:
                while True:
                    try:
                        fix = int(input("1-9: "))
                        if 1 <= fix <= 9:
                            break
                    except ValueError:
                        print("")
            arccosh(value, fix)

        elif users_input == 5:
            value = float(input("enter a value tanh"))
            type = input("enter a type")
            fix = 0
            if fix_key == 1:
                while True:
                    try:
                        fix = int(input("1-9: "))
                        if 1 <= fix <= 9:
                            break
                    except ValueError:
                        print("")
            tanh(value, fix)

        elif users_input == 6:
            value = float(input("enter a value tanh⁻¹"))
            type = input("enter a type")
            fix = 0
            if fix_key == 1:
                while True:
                    try:
                        fix = int(input("1-9: "))
                        if 1 <= fix <= 9:
                            break
                    except ValueError:
                        print("")
            arctanh(value, fix)


if __name__ == "__main__":
    Hype_button(1,1, 1)




















