import math as mp
import MODES_BUTTON
import Shift_Alpha


memory = {}


def negation(Input):
    return -Input


def negation_complex_shift(shift_key):
    return "∠" if shift_key == 1 else '-'


def real_imaginary(r, theta):
    if negation_complex_shift(Shift_Alpha.shift()) == "∠":
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
        return r,theta


def handle_error(input_sequence):
    if len(input_sequence) == 0 or input_sequence[-1] in ['∠', '-']:
        print("Syntax Error")
        return "Syntax Error"

    elif input_sequence.count('∠') > 1 or input_sequence.count('-') > 1:
        print("Math Error")
        return "Math Error"

    elif input_sequence[0] == '∠':
        print("Syntax Error")
        return "Syntax Error"

    elif '∠' in input_sequence and input_sequence.index('∠') == len(input_sequence) - 1:
        print("Syntax Error")
        return "Syntax Error"

    return None


def negation_button(input_sequence):
    if Shift_Alpha.shift() == -1 and Shift_Alpha.alpha() == -1:
        if MODES_BUTTON.get_current_mode() == "NORM":
            if handle_error(input_sequence):
                return "Math Error"
            input_value = input_sequence[-1]
            negated_value = negation(input_value)
            return f"Input: {input_sequence}, Result: {negated_value}"

        else:
            return "Math Error"

    elif Shift_Alpha.shift() == 1 and Shift_Alpha.alpha() == -1:

        if MODES_BUTTON.get_current_mode() == "CMPLX":
            if handle_error(input_sequence):
                return "Math Error"
            if len(input_sequence) == 2:
                result = real_imaginary(input_sequence[0], input_sequence[1])
                return f"Input: {input_sequence}, Result: {result}"
            else:
                return "Syntax Error"
        else:
            return "Math Error"

    elif Shift_Alpha.alpha() == 1:
        memory['A'] = input_sequence[-1] if input_sequence else None
        return f"Stored in A: {memory['A']}"

    elif Shift_Alpha.alpha() == 1 and MODES_BUTTON.get_current_mode() == "BaseN":
        return "A (Hex)"

    return "Math Error"


if __name__ == "__main__":
    # Test the main function with input sequence "3/4"
    print(negation_button("3/4"))