import numpy as np
import math as mp
import Shift_Alpha
def rand():
    print("Random function called.")
    return "Some result"

def zero_button():
    if Shift_Alpha.shift() == 1:
        result = rand()
        print(result)
    elif Shift_Alpha.alpha() == 1:
        pass
    else:
        return 0

if __name__ == "__main__":
    result = zero_button()
    if result is not None:
        print(result)
