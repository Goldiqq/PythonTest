import math
import tkinter as tk
#Выполнила Макаренко Александра Александровна, группа 44-22-120, вариант №18
def calс():
    x = int(x_n.get())
    if x > 1:
        y = math.sin(math.sqrt(x))
    else:
        y = math.cos(x ** 2)
    ytext.config(text="y = " + str(y))

root = tk.Tk()
input = tk.Frame(root)
input.pack(padx=10, pady=10)

text_x = tk.Label(input, text="x = ")
text_x.pack(side=tk.LEFT)

x_n = tk.Entry(input)
x_n.pack(side=tk.LEFT)

btn = tk.Button(root, text="Вычислить", command=calс)
btn.pack(padx=10, pady=10)

ytext = tk.Label(root, text="")
ytext.pack(padx=10, pady=10)

root.mainloop()
