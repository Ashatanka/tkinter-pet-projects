import tkinter as tk
import ttkbootstrap  as ttk

# create a window
window = ttk.Window(themename='darkly')
window.title('Widget\'s connection')
window.geometry('1000x1000')

# WIDGET TYPES AND VAR TYPES
# # tk text
# text = tk.Text(master=window)
# text.pack()

# # ttk entry
# entry_input = tk.StringVar(value='start value')
# entry = ttk.Entry(master=window, textvariable=entry_input)
# entry.pack()

# # ttk label
# label = ttk.Label(master=window,  text='my label', textvariable=entry_input)
# label.pack()

# # ttk Frame
# frame = ttk.Frame(master=window)
# frame.pack()

# # ttk buttons
# def button_func():
#     entry_text = entry_input.get()
#     #label.configure(text=entry_text)
#     label['text'] = entry_text
#     entry['state'] = 'disabled'

# def button2_func():
#     label['text'] = 'some text'
#     entry['state'] = 'enabled'

# button = ttk.Button(master=frame, text='block entry', command=button_func)
# button.pack(side='left', padx=5)

# button2 = ttk.Button(master=frame, text='cancel', command=button2_func)
# button2.pack(side='left', padx=5)

# button3 = ttk.Button(master=frame, text='good', command=lambda: print('goooood'), textvariable=entry_input)
# button3.pack(side='left', padx=5)

# # ttk checkbutton
# check1_var = tk.BooleanVar()
# check1 = ttk.Checkbutton(window,
#                          text='test checkbutton',
#                          variable=check1_var,
#                          offvalue=0,
#                          onvalue=1,
#                          command=lambda: print(radiotest_var.get()))
# check1.pack()

# # ttk radio buttons - must havee dif values
# def radio_func():
#     print(check1_var.get())
#     check1_var.set(0)

# def func(parameter):
#     print(parameter.get())

# radiotest_var = tk.StringVar()
# radiotest1 = ttk.Radiobutton(window, text='test radiobutton 1',value='A',command=lambda: func(radiotest_var), variable=radiotest_var)
# radiotest1.pack()
# radiotest2 = ttk.Radiobutton(window, text='test radiobutton 2',value='B',command=radio_func, variable=radiotest_var)
# radiotest2.pack()

# # ttk menu
# items = ('Ice cream', 'Pizza', 'Broccoli')
# food_string = tk.StringVar(value=items[0]) # by default ice cream will be selected
# combo = ttk.Combobox(window, textvariable=food_string)
# combo['values'] = items
# combo.pack()

# # ttk spinbox
# spin_int = tk.IntVar(value=11)
# spin = ttk.Spinbox(window, 
#                    from_=3, 
#                    to= 20, 
#                    increment=3, 
#                    command=lambda: print(spin_int.get()),
#                    textvariable=spin_int) # increment = step
# # spin['value'] = (1,2,3,4,5)
# # spin['value'] = ('A', 'B', 'C')
# spin.pack()

# EVENTS
# # list of events https://www.pythontutorial.net/tkinter/tkinter-event-binding/

# text = tk.Text(window)
# text.pack()

# entry = ttk.Entry(window)
# entry.pack()

# button = ttk.Button(window, text='A button')
# button.pack()

# label = ttk.Label(window,  text='my label')
# label.pack()

# # keyboard inputs
# window.bind('<Alt-KeyPress-a>', lambda event: print('Alt+a event')) # event is automatically passing arg
# window.bind('<Any-KeyPress-a>', lambda event: print('"a" pressed event'))
# window.bind('<KeyPress>', lambda event: print(f'any button pressed {event.char}'))

# # widgets getting changed
# combo.bind('<<ComboboxSelected>>', 
#            lambda event: label.configure(text=f'{food_string.get()} is selected')) # to compile uncomment ttk menu and label
# spin.bind('<<Increment>>', lambda event: print("up")) # to compile uncomment ttk spinbox
# spin.bind('<<Decrement>>', lambda event: print("down"))

# # widgets gets (un)selected
# entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
# entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))
# button.bind('<Alt-KeyPress-b>', lambda event: print('Alt+b and button selected event'))

# # mouse click / wheel / motion
# def get_pos(event):
#     print(f'x: {event.x} y: {event.y}')
# # window.bind('<Motion>', get_pos) # event is automatically passing arg
# text.bind('<Motion>', get_pos) # event is automatically passing arg

# run window - updates the gui and checking  for events
window.mainloop()