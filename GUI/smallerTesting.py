import tkinter as tk

root = tk.Tk()

# Create some widgets
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Place them in the grid
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0, columnspan=2)

# Configure the grid's columns and rows
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=2)

root.mainloop()
