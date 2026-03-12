import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("500x400")

header = tk.Label(window, text="Calculator",bg="pink",font=("Poppins", 20, "bold"))
header.grid(row=0, column=0, columnspan=2, pady=30)

tk.Label(window, text="First Num").grid(row=1, column=0, pady=5)
first_entry = tk.Entry(window)
first_entry.grid(row=1, column=1)

tk.Label(window, text="Second Num").grid(row=2, column=0, pady=5)
second_entry = tk.Entry(window)
second_entry.grid(row=2, column=1)

def add():
    x = float(first_entry.get())
    y = float(second_entry.get())
    header.config(text=f"The sum of {x} and {y} is {x + y}")

def subtract():
    x = float(first_entry.get())
    y = float(second_entry.get())
    header.config(text=f"The difference of {x} and {y} is {x - y}")

def multiply():
    x = float(first_entry.get())
    y = float(second_entry.get())
    header.config(text=f"The product of {x} and {y} is {x * y}")

def divide():
    x = float(first_entry.get())
    y = float(second_entry.get())
    if y != 0:
        header.config(text=f"The quotient of {x} and {y} is {x / y}")
    else:
        header.config(text="Error")

tk.Button(window, text="Add", command=add).grid(row=3, column=0, pady=10)
tk.Button(window, text="Subtract", command=subtract).grid(row=3, column=1, pady=10)
tk.Button(window, text="Multiply", command=multiply).grid(row=4, column=0, pady=10)
tk.Button(window, text="Divide", command=divide).grid(row=4, column=1, pady=10)

window.mainloop()
