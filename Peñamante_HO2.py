import tkinter as tk

window = tk.Tk()
window.title("Jimoh Evar's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg = "Green")

label = tk.Label(window, text = "Student Profile", font = ("Times New Roman",35,"bold"),
fg = "black", bg = "white", anchor = "center")
label.pack(padx = 10, pady = 20)
label = tk.Label(window, text = "Name: Jimoh Evar Peñamante", font = ("Times New Roman",20),
fg = "black", bg = "white")
label.pack(padx = 10, pady = 20, anchor = "nw")

label = tk.Label(window, text = "Age: 19 years old", font = ("Times New Roman",20),
fg = "black", bg = "white")
label.pack(padx = 10, pady = 20, anchor = "nw")

label = tk.Label(window, text = "Course: BSIT", font = ("Times New Roman",20),
fg = "black", bg = "white")
label.pack(padx = 10, pady = 20, anchor = "nw")

label = tk.Label(window, text = "Birthday: November 7, 2006", font = ("Times New Roman",20),
fg = "black", bg = "white")
label.pack(padx = 10, pady = 20, anchor = "nw")

label = tk.Label(window, text = "Motto: ", font = ("Times New Roman",20),
fg = "black", bg = "white")
label.pack(padx = 10, pady = 20, anchor = "nw")

label = tk.Label(window, text = "One Step at a time.",
font = ("Times New Roman",20, "italic"), fg = "black", bg = "white")
label.pack(padx = 10, pady = 20, anchor = "center")

window.mainloop()