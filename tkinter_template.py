import tkinter as tk
import ttkbootstrap  as ttk
from random import choice # to pick 1 random value from list

# create a window
# window = tk.Tk()
window = ttk.Window(themename='darkly')
# window = ttk.Window(themename='flatly')
window.title('Widget\'s connection')
window_height = 1000
window_width = 1000
left = int(window.winfo_screenwidth()/2 - window_width/2)
top = int(window.winfo_screenheight()/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}') # widthxheight+left+top
window.iconbitmap('images\/bee_icon-icons.com_60722.ico')

# # window sizes
# window.minsize(200, 100)
# window.maxsize(1000, 1000)
# window.resizable(True, False) #scale x, scale y

# # screen attributes
# print(window.winfo_screenwidth()) # monitor x size
# print(window.winfo_screenheight()) # monitor y size

# # window attributes
# window.attributes('-alpha', 0.5) # tranceparency
# window.attributes('-topmost', True) # always on top of other windows

# # security event
# window.bind('<Escape>', lambda event: window.quit()) # quit when escaape is pressed
# window.attributes('-disable', True) # we cant interact with window anymore
# window.attributes('-fullscreen', True)

# title bar
# window.overrideredirect(True) # hide menu off the window
grip = ttk.Sizegrip(window)
# grip.pack(side='bottom', anchor='e') # anchor = 'east' position of bottom. n, ne, e, se, s, sw, w, nw, or center
grip.place(relx=1.0, rely=1.0, anchor='se') # south east


# LAYOUTS

label1 = ttk.Label(window, text= 'Label 1', background='red')
label2 = ttk.Label(window, text= 'Label 2', background='blue')

# pack
button = ttk.Button(window, text='Button', command=lambda:print('Button pressed'))
label3 = ttk.Label(window, text='Last of the labels', background='green')

# label1.pack(side='left', expand=True, fill= 'both') # expand = take all availiable space
# label2.pack(side='right', fill='both')
label1.pack(expand=True, fill='both', padx=10, pady = 10)
label2.pack(side='left', expand=True, fill= 'both')
label3.pack(expand=True, fill= 'both'), 
button.pack(expand=True, fill= 'both')

# # grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0,weight=1)
# window.rowconfigure(1,weight=1)

# label1.grid(row=0,column=1,sticky='nsew') # stick to left, right, bottom and top
# label2.grid(row=1,column=1, columnspan=2, sticky='nsew') # take 2 columns starting on column 1

# # place
# label1.place(x=100,y=200, width=200,height=100) # top left position
# # relx: windwow size is from 0 to 1. label pos relative to current win size
# # relwidth: width relative to current window width
# # anchor = placing position is pos of topleft coordinates by default. but we can place by center pos, nsew pos
# label2.place(relx=0.5, rely=0.5, relwidth=0.5, anchor='center') 

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
# frame = ttk.Frame(master=window, width=100, height=200, borderwidth=10, relief=tk.GROOVE)
# frame.pack_propagate(False) # dont change setted width and height by children element
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

# # canvas
# canvas = tk.Canvas(window, bg='white', width=250, height=250)
# canvas.pack()

# canvas.create_polygon((0,0,100,200,300,50, 150,-50), fill='black')  
# canvas.create_rectangle((50, 20, 100, 200),fill= 'grey', width=10, dash= (4,4), outline='yellow') # width = border width
# canvas.create_line((0,0,100,150), fill='blue')
# canvas.create_oval((0,0,100,100), fill='blue')
# canvas.create_arc((0,0,100,100), 
#                   fill='red',  
#                   start = 90, # start - degrees to rotate left
#                   extent = 90, # default arc degree is 90 (1/4 of circle)
#                   # style = tk.ARC, # no fill, just border
#                   style = tk.CHORD, # to fill circle without touching the center
#                   outline = 'red',
#                   width = 1)
# canvas.create_text((200,200), text='some text', fill='green', width=50, font='24') # x,y of center of text

# canvas.create_window((50,100), window=ttk.Button(window,text='Button in a canvas'))

# # treeview (table)
# first_col = ['Mary', 'Natalie', 'Sergay', 'Nikita', 'Ivan']
# second_col = ['Sarzhanov', 'Myaskov', 'Mizurev', 'Keller', 'Milovzorov']
# table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
# table.heading('first', text='Name')
# table.heading('last', text='Surname')
# table.heading('email', text='Email')
# table.pack(fill='both', expand=True)

# for i in range(100):
#     first = choice(first_col)
#     last = choice(second_col)
#     email = f'{first[0]}{last}@email.com'
#     data = (first, last, email)
#     table.insert(parent='', index=0,values=data) # index = string num (from 0)

# table.insert(parent='', index=tk.END,values=('XXXXXX', 'YYYYYY', 'ZZZZZZ')) # tk.END = end of the table

# def item_select(_):
#     print(table.selection())
#     for i in table.selection():
#         print(table.item(i)['values'])

# def delete_items(_):
#     for i in table.selection():
#         print(i)
#         table.delete(i)

# table.bind('<<TreeviewSelect>>', item_select)
# table.bind('<Delete>', delete_items)

# # ttk slider
# scale_float = tk.DoubleVar(value=15)
# scale = ttk.Scale(window, 
#                   command=lambda value: progress.stop(), 
#                   from_=0, 
#                   to=25,
#                   length=300,
#                   orient='vertical',
#                   variable=scale_float)
# scale.pack()

# # progress bar
# progress = ttk.Progressbar(window, 
#                            maximum=25,
#                            variable=scale_float,
#                            orient='horizontal',
#                            mode='indeterminate', # determinate by default
#                            length=400) 
# progress.pack()

# progress.start(1000) # moves once in 1000ms

# # scrolledtext
# scrolled_text = tk.scrolledtext.ScrolledText(window, width=100, height=5) # or from tkinter import scrolledtext
# scrolled_text.pack()

# # notebook (tab widget)
# notebook = ttk.Notebook(window)

# tab1 = ttk.Frame(notebook)
# label = ttk.Label(tab1, text= 'Text in tab 1')
# button = ttk.Button(tab1, text='Button in tab 1')
# label.pack()
# button.pack()

# tab2 = ttk.Frame(notebook)
# label2 = ttk.Label(tab2, text= 'Text in tab 2')
# entry2 = ttk.Entry(tab2)
# label2.pack()
# entry2.pack()

# notebook.add(tab1, text='tab1')
# notebook.add(tab2, text='tab2')

# notebook.pack()

# # tk menu
# menu = tk.Menu(window)

# sub_menu = tk.Menu(menu, tearoff=False)
# sub_menu.add_command(label='New', command=lambda: print('New File'))
# sub_menu.add_command(label='Open', command=lambda: print('Open File'))
# sub_menu.add_separator()
# sub_menu.add_command(label='Close', command=lambda: print('Close File'))
# menu.add_cascade(label='File', menu=sub_menu)

# another_sub_menu = tk.Menu(menu, tearoff=False)
# another_sub_menu.add_command(label='Help entry', command=lambda: print(another_sub_menu_check_string.get()))
# another_sub_menu_check_string = tk.StringVar(value='off')
# another_sub_menu.add_checkbutton(label='check', 
#                                  onvalue='on', 
#                                  offvalue='off', 
#                                  variable=another_sub_menu_check_string, 
#                                  command=lambda: print(another_sub_menu_check_string.get()))
# menu.add_cascade(label='Help', menu=another_sub_menu)

# exercise_sub_menu = tk.Menu(menu, tearoff=False)
# radiotest_var = tk.StringVar()
# exercise_sub_menu.add_radiobutton(label='radio1', value='A', variable=radiotest_var)
# exercise_sub_menu.add_radiobutton(label='radio2', value='B', variable=radiotest_var)
# exercise_sub_menu.add_separator()
# sub_sub_menu = tk.Menu(exercise_sub_menu, tearoff=False)
# sub_sub_menu.add_command(label='Option 1', command=lambda: print('Option 1'))
# sub_sub_menu.add_command(label='Option 2', command=lambda: print('Option 2'))
# exercise_sub_menu.add_cascade(label='Other', menu=sub_sub_menu)
# menu.add_cascade(label='Exercice', menu=exercise_sub_menu)

# window.configure(menu=menu)

# # ttk menu button
# menu_button = ttk.Menubutton(window, text='Menu Button')
# menu_button.pack()

# button_sub_menu = tk.Menu(menu_button, tearoff=False)
# button_sub_menu.add_command(label='entry 1', command=lambda: print('test1'))
# button_sub_menu.add_checkbutton(label='check 1')
# menu_button.configure(menu=button_sub_menu)


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