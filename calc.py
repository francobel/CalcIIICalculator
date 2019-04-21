#   Programmer: Eduardo Belman
#      Project: Vector Calculus Calculator
# Time Elapsed: 18 Hours
#  Days Worked: 3 

import tkinter as tk
from sympy import diff

calc = tk.Tk()
calc.title('Multivariable Calculus Calculator')
calc.geometry("300x400")
calc.resizable(0, 0)

##############################
#
#  Button modifying functions
#
##############################
def start_screen(): #Sets home screen buttons
    button1.place(relx=.5, rely=.3, anchor="c")
    button2.place(relx=.5, rely=.5, anchor="c")
    button3.place(relx=.5, rely=.7, anchor="c")
    answer_lab.place(relx=.5, rely=.1, anchor="c")

def clear_screen():#Clears every menu button
    for i in range(0,14):
        exec("button" + str(i) + ".place_forget()")

    vec1_entry.place_forget()
    vec2_entry.place_forget()
    vec1_entry.delete(first=0, last=30)
    vec2_entry.delete(first=0, last=30)
    calc_button.place_forget()
    sign_label.place_forget()

    answer_lab.config(text="")

def retrn(): #Returns home screen buttons & removes vec alg buttons
    clear_screen()
    button1.place(relx=.5, rely=.3, anchor="c")
    button2.place(relx=.5, rely=.5, anchor="c")
    button3.place(relx=.5, rely=.7, anchor="c")

def va_screen(): #Clears screen and sets the Vector Algebra menu screen
    clear_screen()
    button4.place(relx=.5, rely=.3, anchor="c")
    button5.place(relx=.5, rely=.4, anchor="c")
    button6.place(relx=.5, rely=.5, anchor="c")
    button7.place(relx=.5, rely=.6, anchor="c")
    button8.place(relx=.5, rely=.7, anchor="c")
    button0.place(relx=.5, rely=.8, anchor="c")

def do_screen(): #Sets differential operator buttons and hides home screen buttons
    clear_screen()
    button9.place(relx=.5, rely=.3, anchor="c")
    button10.place(relx=.5, rely=.45, anchor="c")
    button11.place(relx=.5, rely=.6, anchor="c")
    button0.place(relx=.5, rely=.75, anchor="c")

def der_screen(): #Sets derivative buttons and hides home screen buttons
    clear_screen()
    button12.place(relx=.5, rely=.3, anchor="c")
    button13.place(relx=.5, rely=.5, anchor="c")
    button0.place(relx=.5, rely=.7, anchor="c")

def main():
    start_screen()
    calc.mainloop()

##############################
#
#  Classes
#
##############################
class VectorAlgebra:

    operation = ""

    def va_return():
        va_screen()
        button0.config(command=retrn)

    def add_display():
        clear_screen()
        vec1_entry.place(relx=.5, rely=.3, anchor="c")
        sign_label.place(relx=.5, rely=.375, anchor="c")
        vec2_entry.place(relx=.5, rely=.45, anchor="c")
        calc_button.place(relx=.5, rely=.6, anchor="c")
        button0.place(relx=.5, rely=.7, anchor="c")

        sign_label.config(text="+")
        button0.config(command=VectorAlgebra.va_return)
        calc_button.config(command=VectorAlgebra.calculate)
        VectorAlgebra.operation = 0

    def sub_display():
        VectorAlgebra.add_display()
        sign_label.config(text="-")
        VectorAlgebra.operation = 1

    def scalar_display():
        VectorAlgebra.add_display()
        sign_label.config(text="*")
        VectorAlgebra.operation = 2

    def dot_display():
        VectorAlgebra.add_display()
        sign_label.config(text="•")
        VectorAlgebra.operation = 3

    def cross_display():
        VectorAlgebra.add_display()
        sign_label.config(text="x")
        VectorAlgebra.operation = 4

    def calculate():
        vec_list = []
        answer = "("
        vec1 = vec1_entry.get().replace('(',"").replace(')',"")
        vec2 = vec2_entry.get().replace('(',"").replace(')',"")
        vec1Array = vec1.split(',');
        vec2Array = vec2.split(',');


        #Adds the individual vector entries (x1+x2, y1+y2, z1+z2)
        if VectorAlgebra.operation == 0:
            for i in range(len(vec1Array)):
                vec_list.append(int(vec1Array[i]) + int(vec2Array[i]))

        #Subtracts the individual vector entries (x1-x2, y1-y2, z1-z2)
        elif VectorAlgebra.operation == 1:
            for i in range(len(vec1Array)):
                vec_list.append(int(vec1Array[i]) - int(vec2Array[i]))

        #Multiplies the whole vector by a scalar multiple (x*S, y*S, z*S)
        elif VectorAlgebra.operation == 2:
            for i in range(len(vec2Array)):
                vec_list.append(int(vec1Array[0]) * int(vec2Array[i]))

        #Multiplies the individual vector entries and adds them (x1*x2 + y1*y2 + z1*z2)
        elif VectorAlgebra.operation == 3:
            dot_prod = 0
            for i in range(len(vec1Array)):
                dot_prod += int(vec1Array[i]) * int(vec2Array[i])
            vec_list.append(dot_prod)

        #Takes the cross product of the two vectors (y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2)
        elif VectorAlgebra.operation == 4:
            vec_list.append(int(vec1Array[1]) * int(vec2Array[2]) - int(vec1Array[2]) * int(vec2Array[1]))
            vec_list.append(int(vec1Array[2]) * int(vec2Array[0]) - int(vec1Array[0]) * int(vec2Array[2]))
            vec_list.append(int(vec1Array[0]) * int(vec2Array[1]) - int(vec1Array[1]) * int(vec2Array[0]))

        #Appends the list of answers to a string
        for j in vec_list[:-1]:
            answer += str(j) + ","
        answer += str(vec_list[-1]) + ")"

        answer_lab.config(text=answer)

class DifferentialOperators:

    operation = ""

    def do_return():
        do_screen()
        button0.config(command=retrn)

    def gradient_display():
        clear_screen()
        vec1_entry.place(relx=.5, rely=.3, anchor="c")
        calc_button.place(relx=.5, rely=.45, anchor="c")
        button0.place(relx=.5, rely=.55, anchor="c")

        button0.config(command=DifferentialOperators.do_return)
        calc_button.config(command=DifferentialOperators.calculate)
        DifferentialOperators.operation = 0

    def divergence_display():
        DifferentialOperators.gradient_display()
        DifferentialOperators.operation = 1

    def curl_display():
        DifferentialOperators.gradient_display()
        DifferentialOperators.operation = 2

    def calculate():
        vec_list = []
        answer = "("
        if DifferentialOperators.operation == 0:
            function = vec1_entry.get()
            i = str(diff(function, 'x'))
            j = str(diff(function, 'y'))
            k = str(diff(function, 'z'))

            answer = "( " + i + " )i + ( " + j + " )j + ( " + k + " )k"

        elif DifferentialOperators.operation == 1:
            vec1 = vec1_entry.get().replace('(',"").replace(')',"")
            vec1Array = vec1.split(',')
            i = diff(vec1Array[0], 'x')
            j = diff(vec1Array[1], 'y')
            k = diff(vec1Array[2], 'z')

            answer = i+j+k

        elif DifferentialOperators.operation == 2:
            vec1 = vec1_entry.get().replace('(',"").replace(')',"")
            vec_array = vec1.split(',')
            i = str(diff(vec_array[2], 'y') - diff(vec_array[1], 'z'))
            j = str(diff(vec_array[0], 'z') - diff(vec_array[2], 'x'))
            k = str(diff(vec_array[1], 'x') - diff(vec_array[0], 'y'))

            answer = "( " + i + " )i + ( " + j + " )j + ( " + k + " )k"

        answer = answer.replace("**",'^').replace("*","")
        answer_lab.config(text=answer)

class Derivatives:

    operation = ""

    def der_return():
        der_screen()
        button0.config(command=retrn)

    def deriv_display():
        clear_screen()
        vec1_entry.place(relx=.5, rely=.3, anchor="c")
        calc_button.place(relx=.5, rely=.45, anchor="c")
        button0.place(relx=.5, rely=.55, anchor="c")

        button0.config(command=Derivatives.der_return)
        calc_button.config(command=Derivatives.calculate)
        Derivatives.operation = 0

    def partial_display():
        clear_screen()
        Derivatives.deriv_display()
        vec1_entry.place(relx=.5, rely=.3, anchor="c")
        vec2_entry.place(relx=.5, rely=.45, anchor="c")
        calc_button.place(relx=.5, rely=.55, anchor="c")
        button0.place(relx=.5, rely=.65, anchor="c")

        button0.config(command=Derivatives.der_return)
        calc_button.config(command=Derivatives.calculate)
        Derivatives.operation = 1

    def calculate():
        if Derivatives.operation == 0:
            function = vec1_entry.get()
            answer = str(diff(function))
            answer = answer.replace("**",'^').replace("*","")

        elif Derivatives.operation == 1:
            function = vec1_entry.get()
            with_res_to = vec2_entry.get()
            answer = str(diff(function, with_res_to))
            answer = answer.replace("**",'^').replace("*","")

        answer_lab.config(text=answer)

##############################
#
#  Widgets
#
##############################
# I know my button naming
# convention isn't proper butto
# it's like this at the moment
# for the sake of convenience
###############################

#Answer Label
answer_lab = tk.Label(calc, pady = 10, bg = "white", width = "300",  fg = "black")

#Return Button
button0 = tk.Button(calc, text='Return', width=20, command=retrn)

#Main Menu Buttons
button1 = tk.Button(calc, text='Vector Algebra', width=20, command=va_screen)
button2 = tk.Button(calc, text='Differential Operators', width=20, command=do_screen)
button3 = tk.Button(calc, text='Differentiation', width=20, command=der_screen)

#Vector Algebra Buttons
button4 = tk.Button(calc, text='Vector Addition', width=20, command=VectorAlgebra.add_display)
button5 = tk.Button(calc, text='Vector Subtraction', width=20, command=VectorAlgebra.sub_display)
button6 = tk.Button(calc, text='Scalar Product', width=20, command=VectorAlgebra.scalar_display)
button7 = tk.Button(calc, text='Dot Product', width=20, command=VectorAlgebra.dot_display)
button8 = tk.Button(calc, text='Cross Product', width=20, command=VectorAlgebra.cross_display)

#Differential Operator Buttons
button9 = tk.Button(calc, text='Gradient', width=20, command=DifferentialOperators.gradient_display)
button10 = tk.Button(calc, text='Divergence', width=20, command=DifferentialOperators.divergence_display)
button11 = tk.Button(calc, text='Curl', width=20, command=DifferentialOperators.curl_display)

#Derivative Buttons
button12 = tk.Button(calc, text='Derivative', width=20, command=Derivatives.deriv_display)
button13 = tk.Button(calc, text='Partial Derivative', width=20, command=Derivatives.partial_display)

#Vector Addition Widgets
vec1_entry = tk.Entry(calc, width = 22, bg = "white", fg = "black", justify = "center")
vec2_entry = tk.Entry(calc, width = 22, bg = "white", fg = "black", justify = "center")
sign_label = tk.Label(calc, bg = "white", width = "2",  fg = "black", text = "", font=("Times New Roman", 14, 'bold'))
calc_button = tk.Button(calc, text='Calculate', width=20, command=VectorAlgebra.calculate)

if __name__ == "__main__":
    main()
