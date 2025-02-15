import tkinter as tk

def click_button(entry, value):

    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear(entry):

    entry.delete(0, tk.END)

def calculate(entry):

    try:
        result = eval(entry.get())

        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Калькулятор")
    root.configure(bg="#2e2e2e")

    entry = tk.Entry(root, width=20, font=("Consolas", 28, "bold"), borderwidth=2, relief="solid", justify="right", bg="#1c1c1e", fg="#ffffff")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
    ]

    for (text, row, col) in buttons:
        if text == "=":
            button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                               bg="#ff9500", fg="#ffffff", activebackground="#e68900", command=lambda e=entry: calculate(e))
        else:
            button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                               bg="#4a4a4a", fg="#ffffff", activebackground="#5e5e5e",
                               command=lambda e=entry, t=text: click_button(e, t))
        button.grid(row=row, column=col, padx=5, pady=5)

    clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18),
                             bg="#ff3b30", fg="#ffffff", activebackground="#e63329", command=lambda e=entry: clear(e))
    clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="we")

    root.mainloop()