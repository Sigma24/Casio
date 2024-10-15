import math as mp
import MODES_BUTTON
import ShiftKey
import AlphaKey


memory = {}

def negation(Input):
    return -Input

def negation_complex_shift(shift_key):
    return "∠" if shift_key == 1 else '-'

def real_imaginary(r, theta):
    if negation_complex_shift(ShiftKey.shift()) == "∠":
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
        return None

def handle_error(input_sequence, symbol):
    if len(input_sequence) == 0 or input_sequence[-1] in ['∠', '-']:
        print("Syntax Error")
        return True
    elif input_sequence.count('∠') > 1 or input_sequence.count('-') > 1:
        print("Math Error")
        return True
    return False

def negation_button(input_sequence):
    if ShiftKey.shift() == -1 and AlphaKey.alpha() == -1:

        if MODES_BUTTON.get_current_mode() == "NORM":
            if handle_error(input_sequence, '-'):
                return "Math Error"
            negated_value = negation(input_sequence.pop() if input_sequence else None)
            input_sequence.append(negated_value)
            return input_sequence
        else:
            print("Math Error")
            return "Math Error"

    elif ShiftKey.shift() == 1 and AlphaKey.alpha() == -1:

        if MODES_BUTTON.get_current_mode() == "CMPLX":
            if handle_error(input_sequence, '∠'):
                return "Math Error"
            return real_imaginary(input_sequence[0], input_sequence[1]) if len(input_sequence) == 2 else "Syntax Error"
        else:
            return "Math Error"

    elif AlphaKey.alpha() == 1:

        memory['A'] = input_sequence[-1] if input_sequence else None
        return "A"

    elif AlphaKey.alpha() == 1 and MODES_BUTTON.get_current_mode() == "BaseN":

        return "A (Hex)"

    return "Math Error"


