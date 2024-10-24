from BUTTON_1 import one_button
from BUTTON_2 import Two_Button
from BUTTON_3 import Three_Button
from BUTTON_4 import Four_Button
from BUTTON_5 import Five_Button
from BUTTON_6 import Six_Button
from BUTTON_7 import Seven_Button
from BUTTON_8 import eight_Button
import Shift_Alpha


# Global variable to store the selected mode
selected_mode = 'DEG'

def set_mode(mode):
    global selected_mode
    selected_mode = mode

def get_current_mode():
     return selected_mode

def Mthio():
    set_mode("MTHIO")
    print("Switched to MTHIO Mode")

def lineio():
    set_mode("LINEIO")
    print("Switched to LINEIO Mode")

def Deg():
    set_mode("DEG")
    print("Switched to Degree Mode")

def Rad():
    set_mode("RAD")
    print("Switched to Radian Mode")

def grad():
    set_mode("GRAD")
    print("Switched to Gradient Mode")

def fix():
    set_mode("FIX")
    print("Switched to Fixed Mode")

def scl():
    set_mode("SCI")
    print("Switched to Scientific Mode")

def norm():
    set_mode("NORM")
    print("Switched to Normal Mode")

def comp():
    set_mode("COMP")
    print("Switched to Comp Mode")

def cmplx():
    set_mode("CMPLX")
    print("Switched to CMPLX Mode")

def stat():
    set_mode("STAT")
    print("Switched to Statistical Mode")

def base_n():
    set_mode("BASE-N")
    print("Switched to Base-N Mode")

def eqn():
    set_mode("EQN")
    print("Switched to Equation Mode")

def matrix():
    set_mode("MATRIX")
    print("Switched to Matrix Mode")

def table():
    set_mode("TABLE")
    print("Switched to Table Mode")

def vector():
    set_mode("VECTOR")
    print("Switched to Vector Mode")

def Mode_Shift():
    print("Select Mode:")
    print("1: MTHIO             2: LINEIO")
    print("3: DEG               4: RAD")
    print("5: GRAD              6: FIX")
    print("7: SCI               8: NORM")

    if one_button() == 1:
        Mthio()
    elif Two_Button() == 2:
        lineio()
    elif Three_Button() == 3:
        Deg()
    elif Four_Button() == 4:
        Rad()
    elif Five_Button() == 5:
        grad()
    elif Six_Button() == 6:
        fix()
    elif Seven_Button() == 7:
        scl()
    elif eight_Button() == 8:
        norm()
    else:
        print("Invalid selection, please try again.")

def MODE():
    print("Select Calculator Mode:")
    print("1: COMP              2: CMPLX")
    print("3: STAT              4: BASE-N")
    print("5: EQN               6: MATRIX")
    print("7: TABLE            8: VECTOR")

    if one_button() == 1:
        comp()
    elif Two_Button() == 2:
        cmplx()
    elif Three_Button() == 3:
        stat()
    elif Four_Button() == 4:
        base_n()
    elif Five_Button() == 5:
        eqn()
    elif Six_Button() == 6:
        matrix()
    elif Seven_Button() == 7:
        table()
    elif eight_Button() == 8:
        vector()
    else:
        print("Invalid selection, please try again.")

def mod_button():
    if Shift_Alpha.shift() == -1 and Shift_Alpha.alpha() == -1:
        MODE()
    elif Shift_Alpha.shift() == 1:
        Mode_Shift()
    elif Shift_Alpha.alpha() == 1:
        print("Alpha key function not implemented.")
    else:
        print("No valid key pressed.")


if __name__ == "__main__":
    mod_button()
