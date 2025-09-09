import tkinter as tk

root = tk.Tk()
root.title('Third Tkinter App')
root.geometry('800x600+1300+300')
root.configure(bg = 'lightgray')

# Event Sequence Syntax
# "<EventType-Detail>"
# Mouse: 
#   "<Button-1>" (left click)
#   "<Button-2>", "<Button-3>", "<Double-1>", <"B1-Motion>" (drag while left held)
#   "<Enter>" / "<Leave>" (pointer enters/leaves widget)
# Keyboard:
#   "<Key>" (any key)
#   "<KeyPress-Return>", "<KeyRelease-a>", "<Control-c>", "<Shift-Tab>"

# Binding Targets
# widget.bind(seq, fn) - only that widget
# root.bind(seq, fn) - the root window
# root.bind_all(seq, fn) - the whole app (global)

# The event object (callback signature fn(event))
# event.x, event.y (widget coords)
# event.x_root, event.y_root (screen)
# event.keysym (symbolic key like "a", "Return")
# event.keycode (platform code)
# event.widget (source widget)

# Events bubble up widget -> parent -> toplevel
# Return the string "break" from your handler to stop further processing
# Some widgets already bind default behaviors (Entry handles text input). Returning "break" prevents the default action

def show_coord(event):
  window_x = event.x_root - root.winfo_rootx() # x_root and y_rrot are screen coord
  window_y = event.y_root - root.winfo_rooty()
  coord_label.config(text = f"x: {window_x}, y: {window_y}")

label = tk.Label(root, text = "Move mouse here to see its coord in window", bg = "lightblue", height = 8)
label.bind("<Motion>", show_coord)
label.pack(side = "top", fill = "x")

coord_label = tk.Label(root, text = "Coord will show here", bg = "lightgreen")
coord_label.pack(side = "bottom", expand = True, fill = "both")


root.mainloop()