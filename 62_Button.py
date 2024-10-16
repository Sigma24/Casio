import math as mp

import MODES_BUTTON
import ShiftKey
import AlphaKey

memory = {}


def simple_degree_min_second(decimal_value):
    degrees = int(decimal_value)


    minutes_full = abs(decimal_value - degrees) * 60
    minutes = int(minutes_full)


    seconds = (minutes_full - minutes) * 60



    return f"{degrees}°{minutes}' {round(seconds,1)}\""


def DMS_button():
    if  AlphaKey.alpha()==1:
        return f"stored in b {memory['b']}"
    elif AlphaKey==1 and  MODES_BUTTON.get_current_mode()=="BaseN":
        return 'Hexa B'


if __name__ == "__main__":

  print(simple_degree_min_second(23.36))


