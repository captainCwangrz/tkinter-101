import tkinter as tk

root = tk.Tk()
root.title("Second Tkinter App")
root.geometry("800x600+1300+300")
root.configure(bg = "lightgray")

# Label
# Displays static or dynamic text or even images
# Important params: text, fg, bg, font
label = tk.Label(root, text = "Hello, Tkinter! This is a label", bg = 'lightblue')

# Entry
# A single-line text field. Perfect for user input
# Use .get() to retrieve text, .delete(0, tk.END) to clear it, .insert(0, "default") to pre-fill
entry = tk.Entry(root)
entry.insert(0, "This is an entry")

# Text
# Multi-line text editor
# Like Entry but supports larger input, scrolling, and formatting
# User .get("1.0", tk.END) (line 1, char 0 to the end) to retrieve its contents
text = tk.Text(root, height = 5, width = 30)
text.insert("0.0", "This is a text box")

# Button
# Executes a function when clicked
# The command function expects a callable with no parentheses
def some_function():
  pass 
button = tk.Button(root, text = "Click Me. I'm a button", command = some_function)



# Geometry Managers
# pack()
# Simplest. Places widgets relative to each other (top, bottom, left, right)
# Good for vertical / horizontal stacking
# Options: side, fill (x, y, both, none), expand

# grid()
# Places widgets in a 2D grid (rows and columns)
# More precise, ideal for forms or calculators
# Don't mix pack and grid in the same parent!

# place()
# Absolute positioning. You tell it the pixel coordinates
# Useful for custom layouts, but fragile if window resizes

# Rule of thumb: start with pack, graduate to grid. Use place sparingly

label.pack(side = "top", fill = 'both', expand = True)
entry.pack(side = "top", fill = 'both', expand = True)
text.pack(side = "top", fill = 'both', expand = True)
button.pack(side = "top", fill = 'both', expand = True)

root.mainloop()