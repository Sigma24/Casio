shift_key = -1
alpha_key = -1
def shift():
    global shift_key
    global alpha_key
    if shift_key == -1:
        shift_key = 1
        alpha_key = -1
    else:
        shift_key = -1

    return shift_key