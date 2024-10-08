import math as mp
import MODES_BUTTON

print("DAWOOD")

def negation(Input):
    return -Input

def negation_complex_shift(shift_key):
    if shift_key == 1:
        return "∠"
    else:
        return '-'


def real_imaginary(r, theta):
    if negation_complex_shift(1) == "∠":
        if MODES_BUTTON.get_current_mode() == "DEG":
            theta_rad = mp.radians(theta)
            real_part = r * mp.cos(theta_rad)
            imag_part = r * mp.sin(theta_rad)
            return complex(real_part, imag_part)

        elif MODES_BUTTON.get_current_mode() == "RAD":
            real_part = r * mp.cos(theta)
            imag_part = r * mp.sin(theta)
            return complex(real_part, imag_part)

        else:
            theta_rad = theta * (mp.pi / 200)
            real_part = r * mp.cos(theta_rad)
            imag_part = r * mp.sin(theta_rad)
            return complex(real_part, imag_part)

    else:
        print("Math Error")


def Negation_button(shift_key, alpha_key):
    # Ensure only one key is active (the last pressed key remains active)
    if shift_key == 1 and alpha_key == 1:
        if last_pressed == 'shift':
            alpha_key = 0
        else:
            shift_key = 0

    MODES_BUTTON.mod_button(0, 0)

    if alpha_key == 1:
        alpha_key = 0
        print("A")

    elif shift_key == 1 or MODES_BUTTON.get_current_mode() == "CMPLX":
        if shift_key == 1:
            alpha_key = 0
        else:
            shift_key = 0
        angle = negation_complex_shift(1)
        print(angle)

    elif shift_key == 0 and MODES_BUTTON.get_current_mode() == "CMPLX":
        print(negation_complex_shift(0))
        inn = input("Enter: ")
        if inn == "":
            inn = None
            print(" ")
        else:
            inn = int(inn)
            print(negation(inn))

    elif shift_key == 0 and MODES_BUTTON.get_current_mode() == "COMP":
        print(negation_complex_shift(0))
        inn = input("Enter: ")
        if inn == "":
            inn = None
            print(" ")
        else:
            inn = int(inn)
            print(negation(inn))

    elif shift_key == 1 and MODES_BUTTON.get_current_mode() == "COMP":
        shift_key = 0
        print(negation_complex_shift(0))
        inn = input("Enter: ")
        if inn == "":
            inn = None
            print(" ")

    else:
        print("Invalid")


# Variable to track the last pressed key
last_pressed = None

# Function to update the last pressed key
def update_last_pressed(key):
    global last_pressed
    last_pressed = key


if __name__ == "__main__":
    # Example usage
    shift_key =0
    alpha_key = 1

    # Simulate key presses
    update_last_pressed('shift')  # Shift key pressed first
    Shift_key = 1
    Negation_button(shift_key, alpha_key)

    update_last_pressed('alpha')  # Alpha key pressed later, shift should become 0
    alpha_key= 0
    Negation_button(shift_key, alpha_key)
