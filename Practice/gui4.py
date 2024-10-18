import tkinter as tk
from tkinter import ttk


# functions
def button_func():
    print(string_var.get())


# window
window = tk.Tk()
window.title("TKInter Variables")
window.geometry('500x500')

# tkinter variable
string_var = tk.StringVar(value="test")

# widgets
label = ttk.Label(window, text="TKInter Variables", textvariable=string_var)
label.pack()

entry = ttk.Entry(window, textvariable=string_var)
entry.pack()

entry2 = ttk.Entry(window, textvariable=string_var)
entry2.pack(pady=1)

button = ttk.Button(window, text="Button", command=button_func)
button.pack()

# run
window.mainloop()
