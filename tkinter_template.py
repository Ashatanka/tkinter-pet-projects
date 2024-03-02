import tkinter as tk
import ttkbootstrap  as ttk

def button_func():
    entry_text = entry_input.get()
    #label.configure(text=entry_text)
    label['text'] = entry_text
    entry['state'] = 'disabled'

def button2_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

# create a window
window = ttk.Window(themename='darkly')
window.title('Widget\'s connection')
window.geometry('1000x1000')

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry_input = tk.StringVar(value='start value')
entry = ttk.Entry(master=window, textvariable=entry_input)
entry.pack()

# ttk label
label = ttk.Label(master=window,  text='my label', textvariable=entry_input)
label.pack()

# ttk Frame
frame = ttk.Frame(master=window)
frame.pack()

# ttk buttons
button = ttk.Button(master=frame, text='block entry', command=button_func)
button.pack(side='left', padx=5)

button2 = ttk.Button(master=frame, text='cancel', command=button2_func)
button2.pack(side='left', padx=5)

button3 = ttk.Button(master=frame, text='good', command=lambda: print('goooood'), textvariable=entry_input)
button3.pack(side='left', padx=5)

# ttk checckbutton
check1_var = tk.BooleanVar()
check1 = ttk.Checkbutton(window,
                         text='test checkbutton',
                         variable=check1_var,
                         offvalue=0,
                         onvalue=1,
                         command=lambda: print(radiotest_var.get()))
check1.pack()

# ttk radio buttons - must havee dif values
def radio_func():
    print(check1_var.get())
    check1_var.set(0)

def func(parameter):
    print(parameter.get())

radiotest_var = tk.StringVar()
radiotest1 = ttk.Radiobutton(window, text='test radiobutton 1',value='A',command=lambda: func(radiotest_var), variable=radiotest_var)
radiotest1.pack()
radiotest2 = ttk.Radiobutton(window, text='test radiobutton 2',value='B',command=radio_func, variable=radiotest_var)
radiotest2.pack()

# run window - updates the gui and checking  for events
window.mainloop()