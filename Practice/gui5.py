import tkinter as tk
from tkinter import ttk


# functions
def button_func():
    print(radio_var.get())


# window
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")
window.resizable(True, True)

# button
button_string = tk.StringVar(value="Button with String Var")

button = ttk.Button(window,
                    command=button_func,
                    textvariable=button_string,
                    )
button.pack()

# check button
check_var = tk.BooleanVar()
check = ttk.Checkbutton(window,
                        text="Button with Checkbutton",
                        command=lambda: print(check_var.get()),
                        variable=check_var)
check.pack()

# radio buttons
radio_var = tk.StringVar()

radio1 = tk.Radiobutton(window,
                        text="Radio button 1",
                        value="radio 1",
                        variable=radio_var,
                        )
radio1.pack()
radio2 = tk.Radiobutton(window,
                        text="Radio button 1",
                        value=2,
                        variable=radio_var,
                        )
radio2.pack()

# run
window.mainloop()
