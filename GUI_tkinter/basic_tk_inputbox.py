import tkinter as tk

root = tk.Tk()          # work as main
root.title("Squares & Roots")

tk.Label(root, text="come on...\nlets Math..!").pack(pady=21)

tk.Label(root, text="Enter your name").pack(pady=15)
name_in = tk.Entry(root)
name_in.pack(pady=10)               # paddy value must be in multiplication of 10s to see difference



root.mainloop()  # mandatory to run the tkinter always must be a last line







