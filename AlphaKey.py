shift_key = -1
alpha_key = -1


def alpha():
    global shift_key
    global alpha_key
    if alpha_key == -1:
        alpha_key = 1
        shift_key = -1
    else:
        alpha_key = -1

    return alpha_key