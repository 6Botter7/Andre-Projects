import tkinter as tk


root = tk.Tk()
frame = tk.Frame(root)


def dosomething():
    mylabel.config(text="Goodbye World")


mylabel = tk.Label(frame, text="Hello World", bg="red")
mylabel.pack(padx=50, pady=50)

mybutton = tk.Button(frame, text="Click Me", command=dosomething)
mybutton.pack(padx=50, pady=50)


frame.pack(padx=5, pady=5)
root.mainloop()
