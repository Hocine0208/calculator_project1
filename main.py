# Project 1: Calculator - Day 1 starter
# Goal: open an empty window titled "Calculator", about 320x420.
# Write the code yourself, then run:  python main.py


import customtkinter as ctk


app = ctk.CTk() # Create the main window
app.title("Calculator") # Set the window title
app.geometry("320x420") # Set the window size


# create the display
display = ctk.CTkEntry(app, 
                       width = 280, 
                       height = 50,
                       font=("Arial", 24),
                       justify="right"
                       )
display.grid(row=0, column=0,columnspan=4,padx=10,pady=10,sticky="ew")

# Button data: (label, row, column)
# 2. Store button labels and positions
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
        height=45
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