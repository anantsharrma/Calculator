import tkinter as tk

def add_to_expression(value):
    current = expression.get()
    expression.set(current + value)

def clear_expression():
    expression.set("")

def backspace():
    current = expression.get()
    expression.set(current[:-1])

def calculate():
    try:
        expr = expression.get()

        # Replace symbols with python-friendly operators
        expr = expr.replace("×", "*").replace("÷", "/")

        result = str(eval(expr))
        expression.set(result)
    except:
        expression.set("Error")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x600")
expression = tk.StringVar()

# Display Entry
entry = tk.Entry(root, textvariable=expression, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipadx=10, ipady=15)

# Button layout
buttons = [
    ("C", 1, 0), ("bksp", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("−", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 20), height=2, width=5,
                        command=calculate, bg="#4CAF50", fg="white")
        btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
    else:
        cmd = (
            clear_expression if text == "C"
            else
            backspace if text == "bksp"
            else
            lambda t=text: add_to_expression(t)
        )
        btn = tk.Button(root, text=text, font=("Arial", 20), height=2, width=5, command=cmd)
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

root.mainloop()
