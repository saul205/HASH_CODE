import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
var= tk.StringVar()
label = tk.Label(frame, textvariable = var)
var.set("Te gusta ipo?")

def negacion():
    var.set("Una pena")
    destruir()

def destruir():
    global frame
    button.destroy()
    button2.destroy()
    root.quit()

def confirmacion():
    var.set("Me alegro")
    destruir()

button = tk.Button(frame,text="Si", command = confirmacion)
button2 = tk.Button(frame, text="No", command = negacion)

label.grid(columnspan = 2)
button.grid(row = 1, sticky = "E")
button2.grid (row = 1, column = 1,sticky = "W")

frame.pack()
root.mainloop()

root.destroy()
