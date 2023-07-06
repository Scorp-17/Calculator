import tkinter as tk
from tkinter import font

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

root = tk.Tk()
root.title("Калькулятор")

# Создание общей панели с окантовкой
panel = tk.Frame(root, bg="RoyalBlue1", bd=2, relief=tk.RAISED)
panel.pack(pady=10)

# Создание виджета Entry
entry_font = font.Font(size=20)
entry = tk.Entry(panel, width=15, font=entry_font)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Создание списка кнопок
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Создание кнопок симметрично на панели
button_font = font.Font(size=15)

for button_text, row, column in buttons:
    if button_text == "=":
        button = tk.Button(panel, text=button_text, width=5, height=2, font=button_font,
                           command=button_equal)
    else:
        button = tk.Button(panel, text=button_text, width=5, height=2, font=button_font,
                           command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

button_clear = tk.Button(panel, text="C", width=5, height=2, font=button_font, command=button_clear)
button_clear.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
