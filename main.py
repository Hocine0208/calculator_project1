# Project 1: Calculator (Python + CustomTkinter)
# UI only: all calculation and state live in logic.py (CalculatorEngine).

import customtkinter as ctk
from logic import CalculatorEngine

engine = CalculatorEngine()

app = ctk.CTk()
app.title("Calculator")
app.geometry("320x420")

# Display (read-only, so the user cannot type letters into it)
display = ctk.CTkEntry(app, width=280, height=50, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
display.configure(state="readonly")


def set_display(text):
    """Replace the display text (a read-only entry must be unlocked briefly)."""
    display.configure(state="normal")
    display.delete(0, "end")
    display.insert(0, text)
    display.configure(state="readonly")


def on_button_click(label):
    set_display(engine.press(label))


# Button data: (label, row, column)
button_data = [
    ("C", 1, 0), ("/", 1, 1), ("*", 1, 2), ("-", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("=", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
    ("0", 5, 0), (".", 5, 2),
]

# Extra size for some buttons: label -> (rowspan, columnspan)
spans = {"0": (1, 2), "=": (3, 1)}

for label, row, column in button_data:
    rowspan, columnspan = spans.get(label, (1, 1))
    button = ctk.CTkButton(
        app,
        text=label,
        height=45,
        command=lambda x=label: on_button_click(x),
    )
    button.grid(
        row=row, column=column,
        rowspan=rowspan, columnspan=columnspan,
        padx=5, pady=5, sticky="nsew",
    )

# Make columns and rows expand evenly
for column in range(4):
    app.grid_columnconfigure(column, weight=1)
for row in range(6):
    app.grid_rowconfigure(row, weight=1)

app.mainloop()
