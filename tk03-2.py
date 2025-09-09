import tkinter as tk

root = tk.Tk()
root.title('Third Tkinter App - 2')
root.geometry('800x600+1300+300')
root.configure(bg = 'lightgray')

# Control Variables (the state backbone)
# Tkinter's Variables classes keep widgets and Python state in sync
# tk.StringVar, tk.IntVar, tk.DoubleVar, tk.BooleanVar
# Use with widget options like textvariable = , variable = 

'''
Example

Auto-updates label as you type in entry because they're 'synced' thru StringVar name
name = tk.StringVar(value = 'Charles')
entry = tk.Entry(root, textvariable = name)
label = tk.Label(root, textvariable = name) 

Read/write
name.set('Ada')
print(name.get())

React to changes (observer pattern)
def on_change(varname, index, mode): # index and mode are usually not that useful, you can get new value by varname.get()
  print(f"variable changed to: {varname.get()}")
name.trace_add('write', on_change)

Other mode keywords for trace_add: "read", "unset"
'''

'''
Click Counter
  Mouse + Keys with reset
  Control variables
'''
def main():
  # Model / State
  count = tk.IntVar(value = 0)
  status = tk.StringVar(value = "Pree Space or Click the button")

  # View
  row1 = tk.Frame(root)
  title = tk.Label(row1, text = "Clicks: ", font = ("Microsoft YaHei", 14))
  count_display = tk.Label(row1, textvariable = count, font = ("Consolas", 32))

  def bump():
    count.set(count.get() + 1)
  row2 = tk.Frame(root)
  inc_button = tk.Button(row2, text = "Increment (+1)", command = bump, height = 8)
  reset_button = tk.Button(row2, text = "Reset (Ctrl+R)", command = lambda: count.set(0), height = 8)

  msg = tk.Label(root, textvariable = status, fg = "gray")

  # Bindings
  root.bind("<space>", lambda e: bump())
  root.bind("<Control-r>", lambda e: count.set(0))
  root.bind("<Escape>", lambda e: root.destroy())
  def count_changed(varname, index, mode):
    status.set(f"Count = {count.get()}")
  count.trace_add("write", count_changed)

  # Pack using frames to groups things up for horizontal layout
  row1.pack(fill = 'both', expand = True)
  title.pack(side = "left")
  count_display.pack(side = "left", fill = 'x', expand=True)
  
  row2.pack(fill = 'both', expand = True)
  inc_button.pack(side = 'left', fill = 'x', expand = True)
  reset_button.pack(side = 'left', fill = 'x', expand = True)
  msg.pack(side = 'top', fill = 'both', expand = True)

  root.mainloop()

if __name__ == "__main__":
  main()