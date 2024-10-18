import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    entry_text: str = entry.get()

    # update the label
    label['text'] = entry_text
    entry['state'] = 'disabled'


def button_func2():
    # update the label
    label['text'] = 'Get it off your chest'
    entry['state'] = '!disabled'
    entry.delete(0, tk.END)


# window
window = tk.Tk()
window.title('Getting & Setting Widgets')
window.geometry('250x150')

# widgets
label = ttk.Label(master=window, text='Get it off your chest')
label.pack(pady=10)

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='Submit', command=button_func)
button.pack()

button2 = ttk.Button(master=window, text='Try again', command=button_func2)
button2.pack()


# run
window.mainloop()
