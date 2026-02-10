from tkinter import*

root = Tk()
root.title("Calculator")

result_displayed = False    

def button_click(num):
    global result_displayed
    if result_displayed:             
        e_input.delete(0, END)
        result_displayed = False   
    current=e_input.get()
    e_input.delete(0, END)
    e_input.insert(0, str(current) + str(num))

def input_clear():
    e_input.delete(0, END)    

def num_addition():
    global f_num, operation
    first_number = e_input.get()
    f_num = int(first_number)
    operation = "add"
    e_input.delete(0, END)

def num_subtraction():
    global f_num, operation
    first_number = e_input.get()
    f_num = int(first_number)
    operation = "sub"
    e_input.delete(0, END)    

def num_multiplication():
    global f_num, operation
    first_number = e_input.get()
    f_num = int(first_number)
    operation = "mul"
    e_input.delete(0, END)

def num_divide():
    global f_num, operation
    first_number = e_input.get()
    f_num = int(first_number)
    operation = "div"
    e_input.delete(0, END)

def equal_to():
    global result_displayed
    second_number = int(e_input.get())
    e_input.delete(0, END)

    if operation == "add":
        e_input.insert(0, f_num + second_number)
    elif operation == "sub":
        e_input.insert(0, f_num - second_number)
    elif operation == "mul":
        e_input.insert(0, f_num * second_number)
    elif operation == "div":
        if second_number != 0:
            e_input.insert(0, f_num / second_number)
        else:
            e_input.insert(0, "It can't be divided by zero.")

    result_displayed = True        

e_input = Entry(root, width=40, borderwidth=2)

button_1= Button(root, text="1", padx=35, pady=35, command=lambda: button_click(1))
button_2= Button(root, text="2", padx=35, pady=35, command=lambda: button_click(2))
button_3= Button(root, text="3", padx=35, pady=35, command=lambda: button_click(3))
button_4= Button(root, text="4", padx=35, pady=35, command=lambda: button_click(4))
button_5= Button(root, text="5", padx=35, pady=35, command=lambda: button_click(5))
button_6= Button(root, text="6", padx=35, pady=35, command=lambda: button_click(6))
button_7= Button(root, text="7", padx=35, pady=35, command=lambda: button_click(7))
button_8= Button(root, text="8", padx=35, pady=35, command=lambda: button_click(8))
button_9= Button(root, text="9", padx=35, pady=35, command=lambda: button_click(9))
button_0= Button(root, text="0", padx=35, pady=35, command=lambda: button_click(0))

button_plus= Button(root, text="+", padx=35, pady=35, command=num_addition)
button_minus= Button(root, text="-", padx=35, pady=35, command=num_subtraction)
button_mul= Button(root, text="*", padx=35, pady=35, command=num_multiplication)
button_divide= Button(root, text="/", padx=35, pady=35, command=num_divide)
button_equal= Button(root, text="=", padx=35, pady=35, command=equal_to)
button_clear= Button(root, text="C", padx=35, pady=35, command=input_clear)

e_input.grid(row=0, column=0, columnspan=4, padx=10, pady=13)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_divide.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_mul.grid(row=4, column=3)

root.mainloop()