import numpy as np
import math as mp
import ShiftKey  # Ensure this points to the correct module
import AlphaKey  # Ensure this points to the correct module

def rand():
    print("Random function called.")
    return "Some result"

def zero_button():
    if ShiftKey.shift() == 1:
        result = rand()
        print(result)
    elif AlphaKey.alpha() == 1:
        pass
    else:
        return 0

if __name__ == "__main__":
    result = zero_button()
    if result is not None:
        print(result)
