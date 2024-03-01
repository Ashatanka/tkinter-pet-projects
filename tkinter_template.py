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
window.geometry('800x500')

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry_input = tk.StringVar()
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

# run window - updates the gui and checking  for events
window.mainloop()