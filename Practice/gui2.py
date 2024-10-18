import tkinter as tk
from tkinter import ttk


def button_func():
    print("A button was pressed")


def button_func2():
    label2 = ttk.Label(master=window, text="Hello")
    label2.pack()


# create a window
window = tk.Tk()
window.title('Window and widgets')
window.geometry('800x500')

# ttk widgets
label = ttk.Label(master=window, text="this is a test")
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk button
# button2 = ttk.Button(master=window, text="my button", command=button_func2)
button2 = ttk.Button(master=window, text="my button", command=lambda: button_func2())
button2.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text="click me", command=button_func)
button.pack()

# run
window.mainloop()
