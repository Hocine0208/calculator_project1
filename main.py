# Project 1: Calculator - Day 1 starter
# Goal: open an empty window titled "Calculator", about 320x420.
# Write the code yourself, then run:  python main.py


import customtkinter as ctk
from logic import calculate


app = ctk.CTk() # Create the main window
app.title("Calculator") # Set the window title
app.geometry("320x420") # Set the window size

start_new_number = True
first_number = None
operator = None

def on_button_click(label):
    global start_new_number, first_number, operator
    

    # Handle number buttons only
    if label.isdigit():
        if start_new_number:
            display.delete(0, "end")
            display.insert(0, label)
        else:
            display.insert("end", label)

        start_new_number = False
    
    # Handle operators
    elif label in ["+", "-", "*", "/"]:
        if display.get() != "":
            first_number = float(display.get())
            operator = label
            start_new_number = True
            
    elif label == "=":
        
        try:
            second_number = float(display.get())
            result = calculate(first_number, operator, second_number)
            
            display.delete(0, "end")
            display.insert(0, str(result))
        except (ValueError, TypeError, ZeroDivisionError):
            display.delete(0, "end")
            display.insert(0, "Error")

        start_new_number = True
    
    elif label == ".":
        if start_new_number:
            display.delete(0, "end")
            display.insert(0, "0.")
            start_new_number = False
        elif "." not in display.get():
            if display.get() == "":
                display.insert(0, "0.")
            else:
                display.insert("end", ".")
    
    elif label == "C":
        display.delete(0, "end")
        first_number = None
        operator = None
        start_new_number = True




# create the display
display = ctk.CTkEntry(app, 
                       width = 280, 
                       height = 50,
                       font=("Arial", 24),
                       justify="right"
                       )
display.grid(row=0, column=0,columnspan=4,padx=10,pady=10,sticky="ew")

# 2 Button data: (label, row, column)
button_data = [
    ("C", 1, 0), ("/", 1, 1), ("*", 1, 2), ("-", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("=", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
    ("0", 5, 0), (".", 5, 2)
]

# 3. Create buttons using a loop
for label, row, column in button_data:
    button = ctk.CTkButton(
        app,
        text=label,
        height=45,
        command=lambda x=label: on_button_click(x)
    )

    # Make zero span two columns
    if label == "0":
        button.grid(
            row=row,
            column=column,
            columnspan=2,
            padx=5,
            pady=5,
            sticky="nsew"
        )
    else:
        button.grid(
            row=row,
            column=column,
            padx=5,
            pady=5,
            sticky="nsew"
        )

# 4. Make the four columns expand evenly
for column in range(4):
    app.grid_columnconfigure(column, weight=1)

# Make all rows expand evenly
for row in range(6):
    app.grid_rowconfigure(row, weight=1)
    
app.mainloop() # Start the event loop