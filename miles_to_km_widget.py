import tkinter as tk
# from  tkinter import ttk
import ttkbootstrap  as ttk # makes all ttk widgets better

def convert():
    # 1m = 1,609km
    mile_input = entry_int.get()
    km = mile_input*1.609
    output_string.set(km)
    # print(f'{miles} miles = {km} kilometers')

# create a window
window = ttk.Window(themename='darkly') # window = tk.Tk() | Now we can add themes to window
window.title('Miles to km')
window.geometry('300x150')

# create title of the app on screen (text object)
title_label = ttk.Label(master=window, text='Miles to  kilometers', font='Calibri 24 bold')
# place created title on a window
title_label.pack()

# create a container of 2 widgets side by side: input filed and button
input_frame = ttk.Frame(master=window)

# create miles integer variable
entry_int = tk.IntVar()
# create input field in input_frame
entry = ttk.Entry(master=input_frame, textvariable=entry_int) # textvariable means where to store entered value
# create button in input_frame
button = ttk.Button(master=input_frame, text= 'Convert', command=convert) #  we dont call the func here (not "convert()"), bc the func is called when pressing the button 

entry.pack(side='left', padx=10) # padx = space added left and right to the entry field
button.pack(side='left')
input_frame.pack(pady=10) # pady = space added up and down to the frame

#create result variable
output_string = tk.StringVar()
# create output label
output_label = ttk.Label(master=window, 
                         text='Result', 
                         font='Calibri 24 bold', 
                         textvariable=output_string)
output_label.pack(pady=5)

# run window
window.mainloop()
