import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, colorchooser

# Menus
# You first make a menubar object: menubar = tk.Menu(root, tearoff = False)
# Then you make submenu objects (File, Edit, Help...): filemenu = tk.Menu(menubar, tearoff = False)
# You populate submenus with commands: filemenu.add_command(label = 'Open...', command = open_file)
# Finally, you attach the menubar to the window: root.config(menu = menubar)
# actual command with label -> submenu -> menu -> root

# Cascading submenu: menubar.add_cascade(label = 'File', menu = filemenu)

# Built-in dialogs
# filedialog (open/save files)
# askopenfilename(...) -> path string or '' if canceld
# asksaveasfilename(...) -> path string or ''
# messagebox (info/warn/errors & Yes/No):
# showinfo, showwarning, showerror, askyesno, askyesnocancel
# colorchooser:
# askcolor(title="Pick") -> (rgb_tuple, #rrggbb) or (None, None) if canceld
# always handle cancel

def main():
  root = tk.Tk()
  root.geometry('600x400+1200+450')

  menubar = tk.Menu(root, tearoff = False)
  file_menu = tk.Menu(menubar, tearoff = False)
  help_menu = tk.Menu(menubar, tearoff = False)
  format_menu = tk.Menu(menubar, tearoff = False)

  def new_file(event = None):
    if not maybe_discard_changes():
      return
    text.delete('1.0', 'end')
    state['path'] = None
    state['dirty'] = False
    text.edit_modified(False)
    set_title()
  file_menu.add_command(label = 'New File', command = new_file, accelerator = 'Ctrl+N')

  def open_file(event = None):
    if not maybe_discard_changes():
      return
    path = filedialog.askopenfilename(
      title = 'Open',
      filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not path:
      return
    try:
      with open(path, 'r', encoding = 'utf-8') as f:
        content = f.read()
    except Exception as e:
      messagebox.showerror('Open Error', f"{e}")
      return
    text.delete('1.0', 'end')
    text.insert('1.0', content)
    state['path'] = path
    state['dirty'] = False
    text.edit_modified(False)
    set_title()
  file_menu.add_command(label = "Open", command = open_file, accelerator = 'Ctrl+O')
  
  def save_file(event = None):
    if state['path'] is None:
      return save_file_as()
    try:
      with open(state['path'], 'w', encoding = 'utf-8') as f:
        f.write(text.get('1.0', 'end-1c'))
    except Exception as e:
      messagebox.showerror('Save Error', f'{e}')
      return
    state['dirty'] = False
    text.edit_modified(False)
    set_title()
  file_menu.add_command(label = 'Save', command = save_file, accelerator = 'Ctrl+S')

  def save_file_as(event = None):
    path = filedialog.asksaveasfilename(
      title = 'Save As',
      defaultextension = '.txt',
      filetypes = [('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not path:
      return
    try:
      with open(path, 'w', encoding = 'utf-8') as f:
        f.write(text.get('1.0', 'end-1c'))
    except Exception as e:
      messagebox.showerror('Save Error', f'{e}')
      return
    state['dirty'] = False
    state['path'] = path
    text.edit_modified(False)
    set_title()
  file_menu.add_command(label = "Save As", command = save_file_as, accelerator = 'Ctrl+Shift+S')

  def pick_text_color():
    _, hexcolor = colorchooser.askcolor(title = 'Pick text color')
    if not hexcolor:
      return
    try:
      start, end = text.index('sel.first'), text.index('sel.last')
    except tk.TclError:
      start, end = 'insert', 'insert +1c'
    tag = 'fgcolor'
    text.tag_configure(tag, foreground = hexcolor)
    text.tag_add(tag, start, end)
  format_menu.add_command(label = 'Text Color', command = pick_text_color)

  def show_about():
    messagebox.showinfo('About', f'tkinter Tutorial Unit 5\n minimal tkinter text editor')
  help_menu.add_command(label = 'About', command = show_about)

  menubar.add_cascade(label = "File", menu = file_menu)
  menubar.add_cascade(label = "Format", menu = format_menu)
  menubar.add_cascade(label = 'Help', menu = help_menu)
  root.config(menu = menubar)

  container = tk.Frame(root)
  container.pack(fill = 'both', expand = True)

  yscroll = ttk.Scrollbar(container, orient = 'vertical')
  text = tk.Text(container, wrap = 'word', undo = True, yscrollcommand = yscroll.set)
  yscroll.config(command = text.yview)
  yscroll.pack(side = 'right', fill = 'y')
  text.pack(side = 'left', fill = 'both', expand = True)

  state = {'path' : None, 'dirty' : False}
  def set_title():
    name = state['path'] if state['path'] else 'Untitled'
    mod = '*' if state['dirty'] else ''
    root.title(f'Tiny Text Editor - {name}{mod}')

  def maybe_discard_changes():
    if not state['dirty']:
      return True
    ans = messagebox.askyesnocancel('Unsaved Changes', 'Save your changes before continuing?')
    if ans is None: # cancel
      return False
    if ans: # save
      save_file()
      return not state['dirty'] # might cancel save
    return True # no save

  def on_modified(_ = None):
    if text.edit_modified():
      state['dirty'] = True
      set_title()
      text.edit_modified(False)

  text.bind('<<Modified>>', on_modified)
  root.bind('<Control-n>', new_file)
  root.bind('<Control-o>', open_file)
  root.bind('<Control-s>', save_file)
  root.bind('<Control-S>', save_file_as)

  text.focus_set()
  set_title()
  root.mainloop()

if __name__ == '__main__':
  main()