import re
from enum import FlagBoundary
from symtable import Symbol

import MODES_BUTTON
import Shift_Alpha



memory = {}
dms_key=1
equal_pressed = False



def toggle_dms_key():
    global dms_key
    dms_key = 1 if dms_key == -1 else -1



def symbol(shift_key):
    if shift_key==1:
        return None
    else:
        return "°"



def simple_degree_min_second(Input_sequence):
      degrees = int(Input_sequence)
      minutes_full = abs(Input_sequence- degrees) * 60
      minutes = int(minutes_full)
      seconds = (minutes_full - minutes) * 60
      return f"{degrees}°{minutes}' {round(seconds,1)}\""


def as_in_input(input_sequence):
    pattern = r'^(\d+)°(\d+°)?(\d+°)?$'
    match = re.match(pattern, input_sequence)

    if not match:
        return "Syntax Error"

    degrees = match.group(1)
    minutes = match.group(2)
    seconds = match.group(3)

    minutes = int(minutes[:-1]) if minutes else 0
    seconds = int(seconds[:-1]) if seconds else 0

    if minutes > 59 or seconds > 59:
        return "Syntax Error"


    return f"{degrees}°{minutes}'{seconds}\""


def decimal_value(input_sequence):
    formatted_input = as_in_input(input_sequence)

    if formatted_input == "Syntax Error":
        return "Syntax Error"

    dms_match = re.match(r'(\d+)°(\d+)\'(\d+)\"', formatted_input)
    degrees = int(dms_match.group(1))
    minutes = int(dms_match.group(2))
    seconds = int(dms_match.group(3))

    decimal_result = degrees + (minutes / 60) + (seconds / 3600)
    return round(decimal_result,8)


def Main(Input_sequence):
    global dms_key , equal_pressed
    if not equal_pressed:
        #      if Shift_Alpha.alpha() == 1 and dms_key==1:
        #          dms_key=-1
        #          return f"stored in b {memory.get('b', 'No value stored')}"
        #      elif Shift_Alpha.alpha() == 1 and MODES_BUTTON.get_current_mode() == "BaseN" and dms_key==1:
        #          dms_key=-1
        #          return 'Hexa B'


        if Input_sequence is None:
            if dms_key == 1:

                dms_key=-1
                return symbol(0)

    if '°' not in Input_sequence:

        if dms_key == -1:
             print(Input_sequence)
        if dms_key == 1:
             print(simple_degree_min_second(float(Input_sequence)))

    if '°' in Input_sequence:
        if dms_key == -1:
            print(as_in_input(Input_sequence))
        if dms_key == 1:
              print(decimal_value(Input_sequence))


if  __name__ == "__main__":
       print(Main(None))




