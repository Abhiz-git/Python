import tkinter as tk

root = tk.Tk()          # work as main
root.title("Squares & Roots")

tk.Label(root, text="come on...\nlets Math..!").pack(pady=21)
def game():
    player_name = name_in.get()
    question_display.config(text=f"Ready, {player_name}? Your question will appear here.")
    enter_answer.config(state=tk.NORMAL)

    print(f"Submited...!! {name_in.get()}")

tk.Label(root, text="Welcome to the Squares and Roots").pack(pady=20)
tk.Label(root, text="Enter your name").pack(pady=15)
name_in = tk.Entry(root)
name_in.pack(pady=10)               # paddy value must be in multiplication of 10s to see difference

button = tk.Button(root, text="Submit", command=game)
button.pack(pady=10)

question_display = tk.Label(root, text="", font=("Helvetica", 14))
question_display.pack(pady=10)

tk.Label(root, text="Your answer: ").pack(pady=5)
enter_answer = tk.Entry(root, state=tk.DISABLED)
enter_answer.pack(pady=5)


root.mainloop()  # mandatory to run the tkinter always must be a last line







