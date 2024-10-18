import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def do_something() -> None:
    user_input: int = entry_int.get()
    program_output: int = user_input + 1
    output_string.set(str(program_output))


# window
window = ttk.Window(themename='darkly')
window.title('THE WORLDS BEST APPLICATION')
window.geometry('500x500')

# title
title_label = tk.Label(master=window, text='THE WORLDS BEST APPLICATION', font='Calibri 20 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Button', command=do_something)
entry.pack()
button.pack()
input_frame.pack()

# output
output_string = tk.StringVar()
output_label = tk.Label(master=window,
                        text='Output',
                        font='Calibri 24',
                        textvariable=output_string)
output_label.pack(pady=5)

# run
window.mainloop()
