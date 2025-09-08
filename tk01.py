import tkinter as tk # there's also tkinter.ttk that gives you styled widgets that match the native OS

# root window. Think of it as the canvas that will host everything else
# Althouth in theory you could create multiple Tk() instances, it's almost always not worth it.
# Use tk.Toplevel() instead if you want extra windwos.
root = tk.Tk() 

# title: what you see in the window's title bar
# geometry: "widthxheight". Optional +x+y can also specify the window's position on the screen
# various options set via configure() or root[] such as bg
root.title("My First Tkinter App")
root.geometry("800x600+1300+400")
root.configure(bg = 'lightgray')

# This is the heartbeat. Once you call it, Tkinter enters an endless loop
# It listens for events from the OS (mouse moves, clicks, key presses, window resizing, etc..)
root.mainloop()

'''
Event-driven programming
  GUIs live inside loops reponding to user actions.
Blcoking
  root.mainloop() never retunrs until the window closes. That's why code after it won't run until the end.
  If you want your program to "do things while alive", you'll need after(), bindings, or threads
'''