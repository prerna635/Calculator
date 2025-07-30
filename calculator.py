import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def delete_last():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get().replace('×', '*').replace('÷', '/')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Div by 0")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
window = tk.Tk()
window.title("Calc")
window.geometry("260x370")  # Slightly larger to fit Delete button
window.resizable(False, False)

# Entry field
entry = tk.Entry(window, font=("Arial", 14), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=3, ipady=5, padx=8, pady=8)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('⌫', 5, 0), ('=', 5, 1, 3)  # Delete and Equal buttons
]

# Create buttons
for (text, row, col, *span) in buttons:
    colspan = span[0] if span else 1
    if text == 'C':
        command = clear_entry
    elif text == '⌫':
        command = delete_last
    elif text == '=':
        command = calculate
    else:
        command = lambda x=text: on_click(x)

    btn = tk.Button(
        window, text=text,
        width=5 * colspan, height=1,
        font=("Arial", 12),
        command=command
    )
    btn.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4)

# Run the app
window.mainloop()

