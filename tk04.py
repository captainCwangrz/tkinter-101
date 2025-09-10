import tkinter as tk
from tkinter import ttk # themed widgets

# Frames = your layout's Lego bricks
# A Frame is just a widget that contains other widgets
# group related controls
# isolate geometry managers (on Frame can use pack, another grid)
# apply shared padding/borders/backgrounds to a whole group

# How to nest pack and grid properly
# At the top level, it's common to pack your major regions (header, main, footer)
# Inside a region Frame, use grid for precise, form-like placement
# If you need another sublayout, create another Frame and repeat

# grid essentials for real apps
# row/column start at 0. You can columnspan/rowspan to stretch across
# sticky controls alignment inside the cell
# n, s, e, w. Combine like 'ew' or 'nsew'
# sticky = 'ew' makes a widget expand left<->right inside its cell
# Weights make rows/columns absorb extra space on resize
# frame.grid_columnconfigure(0, weight = 1)
# Columns with higher weight get more of the spare width. No weight -> stays compact

def main():
  root = tk.Tk()
  root.title("Login Form")
  root.geometry("800x600+1300+300")

  # Outer structure: pack for big regions
  container = ttk.Frame(root, padding = (16, 16, 16, 16))
  container.pack(fill = 'both', expand = True)

  # Optional header area
  header = ttk.Label(container, text = "Welcome", anchor = 'center', font = ('Microsoft YaHei', 14))
  header.pack(fill = 'y', expand = True, pady = (0, 12))

  # Inner form frame uses grid for precise alignment
  form = ttk.Frame(container)
  form.pack(fill = 'x')

  # Variables
  username = tk.StringVar()
  password = tk.StringVar()

  # Row 0: Username label + entry
  ttk.Label(form, text = "Username: ").grid(row = 0, column = 0, sticky = 'e', padx = (0, 8), pady = (0, 8))
  user_entry = ttk.Entry(form, textvariable = username)
  user_entry.grid(row = 0, column = 1, sticky = 'ew', pady = (0, 8))

  # Row 1: Pasasword label + entry
  ttk.Label(form, text = "Password: ").grid(row = 1, column = 0, sticky = 'e', padx = (0, 8), pady = (0, 8))
  password_entry = ttk.Entry(form, textvariable = password, show = '*')
  password_entry.grid(row = 1, column = 1, sticky = 'ew', pady = (0, 8))

  # *** Row/column sizing so entries stretch on resize ***
  form.grid_columnconfigure(0, weight = 0) # label column stays tight
  form.grid_columnconfigure(1, weight = 1) # entry column grows

  # Action row
  actions = ttk.Frame(container)
  actions.pack(fill = 'x', pady = (12, 0))

  # Left: "Show password" checkbox
  show_pw = tk.BooleanVar(value = False)
  def toggle_show():
    password_entry.config(show = '' if show_pw.get() else '*')
  ttk.Checkbutton(actions, text = 'Show password', variable = show_pw, command = toggle_show).pack(side = 'left')

  # Right: buttons group
  btn_row = ttk.Frame(actions)
  btn_row.pack(side = 'right')

  def on_login():
    print('Login attempt: ', username.get(), password.get())
  ttk.Button(btn_row, text = 'Cancel', command = root.destroy).pack(side = 'right')
  ttk.Button(btn_row, text = 'Login', command = on_login).pack(side = 'right')

  # Start with keyboard focus in the username field; Enter to submit
  user_entry.focus_set()
  root.bind('<Return>', lambda e: on_login())

  root.mainloop()

if __name__ == '__main__':
  main()