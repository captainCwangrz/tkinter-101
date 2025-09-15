import tkinter as tk
from tkinter import ttk

def main():
  root = tk.Tk()
  root.title("Unit1-4 Practice")
  root.geometry('600x400+1200+500')

  font_big = ("Microsoft YaHei", 20)

  celcius = tk.StringVar(value = '0.0')
  fahrenheit = tk.StringVar(value = '32.0')

  inputFrame = tk.Frame(root)
  inputFrame.pack(expand = True)

  ttk.Label(inputFrame, text = 'Celcius:', font = font_big).grid(row = 0, column = 0)
  cEntry = ttk.Entry(inputFrame, textvariable = celcius, font = font_big)
  cEntry.grid(row = 0, column = 1, sticky = 'ew')
  
  ttk.Label(inputFrame, text = 'Fahrenheit:', font = font_big).grid(row = 0, column = 2)
  fEntry = ttk.Entry(inputFrame, textvariable = fahrenheit, font = font_big)
  fEntry.grid(row = 0, column = 3, sticky = 'ew')

  inputFrame.columnconfigure(0, weight = 0)
  inputFrame.columnconfigure(2, weight = 0)
  inputFrame.columnconfigure(1, weight = 1)
  inputFrame.columnconfigure(3, weight = 1)

  updating = False
  def c2f(name, index, mode):
    nonlocal updating
    if updating:
      return
    try:
      c = float(celcius.get())
    except ValueError:
      return
    updating = True
    try:
      f = c * 9 / 5 + 32
      fahrenheit.set(f"{f:.2f}")
    finally:
      updating = False 
  celcius.trace_add("write", c2f)

  def f2c(name, index, mode):
    nonlocal updating
    if updating:
      return
    try:
      f = float(fahrenheit.get())
    except ValueError:
      return
    updating = True
    try:
      c = (f - 32) * 5 / 9
      celcius.set(f"{c:.2f}")
    finally:
      updating = False
  fahrenheit.trace_add("write", f2c)


  cEntry.focus_set()
  root.bind("<Escape>", lambda e: root.destroy())

  root.mainloop()

if __name__ == '__main__':
  main()