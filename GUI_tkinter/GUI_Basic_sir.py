import tkinter as tk

window = tk.Tk()        #object/instance of tkinter
window.geometry("500x600")          # size/geometry of window

# as tile is on window so to name title we need to use obj's method (title)
window.title("I am Title")

window.config(bg="yellow") # below the title (window passage) for any change we need to config() the object

tk.Label(window, text="hello welcome to GUI of python", bg="red").pack(pady=20)       # pack is necessary to display any component on GUI




button = tk.Button(window, text="Next Page", bg="black", fg="white")
button.pack(pady=30)
window.mainloop()
