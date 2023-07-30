import tkinter as tk
def button_click(btn_value):
    current_value = display.get()
    new_value = current_value + str(btn_value)
    display.delete(0, tk.END)
    display.insert(0, new_value)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear():
    display.delete(0, tk.END)

# Create a Tkinter window
window = tk.Tk()
window.title("Calculator")

# Create an Entry widget to display the calculator inputs and results
display = tk.Entry(window, width=30, font=("Arial", 10))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for each digit and operator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("/", 4, 3)
]

# Bind button_click function to each button
for btn_value, row, col in buttons:
    button = tk.Button(window, text=btn_value, width=5, height=2,
                       command=lambda value=btn_value: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create equal button and clear button
clear_button = tk.Button(window, text="Clear", width=12, height=2, command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

equal_button = tk.Button(window, text="=", width=12, height=2, command=calculate)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()