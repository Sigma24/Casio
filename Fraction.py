import Shift_Alpha


fraction_key = 1

def toggle_key():
    global fraction_key
    fraction_key = 1 if fraction_key == -1 else -1


def fract(input_sequence):
    if '/' in input_sequence:
        numerator, denominator = input_sequence.split('/')
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "undefined"
        result = numerator / denominator
        return result
    else:
        return "Invalid input format"

def Error_Handle(input_sequence):
    pass

def just_press():
    if  Shift_Alpha .shift() == -1:
        return "▭/▭"
    else:
        return None

def Main(input_sequence):
    if fraction_key == 1:
        result = fract(input_sequence)
        return result

if __name__ == "__main__":
    print(Main("1/0"))
