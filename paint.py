import tkinter as tk
import ttkbootstrap  as ttk

# create a window
#window = tk.Tk()
window = ttk.Window(themename='flatly')
window.configure(background='light grey')
window.title('Widget\'s connection')
window.geometry('1000x1000')

# canvas
canvas = tk.Canvas(window, bg='white', width=990, height=900)
canvas.pack()

frame_btns = ttk.Frame(window, width=990)
frame_btns.pack()

# mouse
mouse_pos_string = tk.StringVar(value='x: 0 y: 0')
mouse_pos = ttk.Label(frame_btns, textvariable=mouse_pos_string)
mouse_pos.pack(side='left', padx=5)

draw_types = ('draw', 'line')
draw_type = ttk.StringVar(value=draw_types[0])
# buttons
btn_line = ttk.Button(frame_btns, text='line', command=lambda: draw_type.set(draw_types[1]))
btn_rect = ttk.Button(frame_btns, text='rect')
btn_oval = ttk.Button(frame_btns, text='oval')
btn_text = ttk.Button(frame_btns, text='text')
btn_draw = ttk.Button(frame_btns, text='draw', command=lambda: draw_type.set(draw_types[0]))
btn_line.pack(side='left', padx=5)
btn_rect.pack(side='left', padx=5)
btn_oval.pack(side='left', padx=5)
btn_text.pack(side='left', padx=5)
btn_draw.pack(side='left', padx=5)

def get_pos(event):
    mouse_pos_string.set(f'x: {event.x} y: {event.y}')

def start_draw_pos(event):
    x_start_pos.set(event.x)
    y_start_pos.set(event.y)
    print(event.x, event.y)

def end_draw_line(event):
    canvas.create_line((x_start_pos.get(), y_start_pos.get(), event.x, event.y), fill='black')

canvas.bind('<Motion>', get_pos)
# def draw_line(event):
#     canvas.create_line((x_start_pos.get(), y_start_pos.get(), event.x, event.y), fill='black')

x_start_pos = ttk.IntVar()
y_start_pos = ttk.IntVar()

canvas.bind('<ButtonPress>', start_draw_pos)
# canvas.bind('<B1-Motion>', draw_line)
canvas.bind('<ButtonRelease>', end_draw_line)

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

window.mainloop()
