import numpy as np
import math as mp
import matplotlib.pyplot as plt

Shift_key = 0
Alpha_key = 0

def cos(input, mode,fix=0):
    if -mp.inf<input<mp.inf:
        if mode == "degree":
            conv = np.radians(input)
            result=np.cos(conv)

        elif mode == 'radian':
            result = np.cos(input)

        elif mode == 'gradian':
            convo = (input * np.pi/200)
            result=np.cos(convo)


        else:
            print("Math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"cos({input}): {rounded_result}")
        cosgraph(input,mode)
        return result
    else:
        print("Math error")
        return None

def cosgraph(v,mode):
    print("About to plot a graph")
    starting=v
    ending=v+2*np.pi if mode == "radian" else v+360
    if not -mp.inf < starting < mp.inf or not -mp.inf < ending < mp.inf:
        print("Math error")
    value= np.linspace(starting,ending,200)
    cal_value = []

    for i in value:
        try:
            if mode == "degree":
                conv = np.radians(i)
                val = np.cos(conv)
                print(f"The cos of {i} in degree is {val}")
            elif mode == "radian":
                val = np.cos(i)
                print(f"The cos of {i} in radian is {val}")
            elif mode == "gradian":
                convo = (i * np.pi / 200)
                val = np.cos(convo)
                print(f"The cos of {i} in gradian is {val}")
            else:
                print("Math error")
                return None

            cal_value.append(val)
        except ValueError:
              print(f"Skipping the value of {i} duo domain error")
              continue


    plt.plot(value, cal_value, label=f"f(cos(x)) of type {mode.capitalize()}")
    plt.xlabel('x')
    plt.ylabel(f'f(cos(x))')
    plt.grid(True)
    plt.legend()
    plt.show()




def arccos(input, mode,fix=0):
    if -1<=input<=1:
        if mode == "degree":
            conv = np.radians(input)
            result = np.arccos(conv)

        elif mode == 'radian':
            result = np.arccos(input)

        elif mode == 'gradian':
            convo = (input * np.pi/200)
            result = np.arccos(convo)


        else:
            print("Math error")
            return None
        if fix <= 0:
            fix = 10
        rounded_result = round(result, fix)
        print(f"cos⁻¹({input}): {rounded_result}")

        arccosgraph(input,mode)
        return result
    else:
        print("Math error")
        return None

def arccosgraph(v,mode):
    print("About to plot a graph")

    if mode == "radian" or mode == "degree":
        starting = max(v - 1, -1)
        ending = min(v + 1, 1)
    else:
        starting = max(v - 1, -1)
        ending = min(v + 1, 1)
    if (starting < -1 or starting > 1) or (ending < -1 or ending > 1):
        print("Math error: Value out of domain.")
        return

    value = np.linspace(starting, ending, 200)
    cal_value = []

    for i in value:
        try:
            if mode == "degree":
                conv = np.radians(i)
                val = np.arccos(np.cos(conv))
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The cos⁻¹ of {i} in degree is {val}")

            elif mode == "radian":
                val = np.arccos(i)
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The cos⁻¹ of {i} in radian is {val}")

            elif mode == "gradian":

                convo = (i * np.pi / 200)
                val = np.arccos(np.cos(convo))
                if np.isnan(val):
                    print(f"Skipping value {i} due to error.")
                    continue
                print(f"The cos⁻¹ of {i} in gradian is {val}")

            else:
                print("Math error: Invalid mode.")
                return

            cal_value.append(val)
        except ValueError:
            print(f"Skipping value {i} due to error.")
            continue

    plt.plot(value, cal_value, label=f"f(cos⁻¹(x)) of type {mode.capitalize()}")
    plt.xlabel('x')
    plt.ylabel(f'f(cos⁻¹(x))')
    plt.grid(True)
    plt.legend()
    plt.show()


# ACTUAL CALL  "def cos_Button(Shift_key,value,mode,fix_key)"
def cos_Button(Shift_key,Alpha_key,fix_key):
    if Alpha_key==1:
        Alpha_key = 0
        return 'E'


    if Shift_key == 1:
        value = float(input("Enter a value for cos⁻¹(x): "))
        type = input("Enter a type: ")
        fix=0
        if fix_key == 1:
            while True:
                try:
                    fix = int(input("1-9: "))
                    if 1 <= fix <= 9:
                        break
                except ValueError:
                    print("")
        arccos(value, type,fix)
        Shift_key=0
    else:
        value = float(input("Enter a value for cos(x): "))
        type = input("Enter a type: ")
        fix=0
        if fix_key == 1:
            while True:
                try:
                    fix = int(input("1-9: "))
                    if 1 <= fix <= 9:
                        break
                except ValueError:
                    print("")
        cos(value, type,fix)



if __name__ == "__main__":
    cos_Button(1, 1, 1)


# Your existing cos and arccos functions here

# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes




# Your existing cos and arccos functions here

# @app.route('/')
# def index():
#     return render_template('Button.html')
#
#
# @app.route('/cos_button', methods=['POST'])
# def cos_button():
#     global Shift_key, Alpha_key
#     data = request.json
#     Shift_key = data['Shift_key']
#     Alpha_key = data['Alpha_key']
#     fix_key = data['fix_key']
#     value = data.get('value', 0)
#     mode = data.get('mode', 'radian')
#
#     # If Alpha key is pressed, unpress Shift key and perform Alpha action
#     if Alpha_key == 1:
#         Shift_key = 0
#         return jsonify({'result': 'Alpha key action: D'})  # Simulate pressing 'D'
#
#     fix = 10  # Default precision
#     if fix_key != 0:
#         fix = fix_key
#
#     # Check if Shift key is pressed for arccos
#     if Shift_key == 1:
#         result = arccos(value, mode, fix)
#     else:
#         result = cos(value, mode, fix)
#
#     return jsonify({'result': result})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
