import tkinter as tk

# Function to handle button clicks
def click_button(event):
    text = event.widget.cget("text")
    current_text = entry.get()

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Define button labels and colors
button_data = [
    ("7", "#d0d0d0"), ("8", "#d0d0d0"), ("9", "#d0d0d0"), ("/", "#ffa500"),
    ("4", "#d0d0d0"), ("5", "#d0d0d0"), ("6", "#d0d0d0"), ("*", "#ffa500"),
    ("1", "#d0d0d0"), ("2", "#d0d0d0"), ("3", "#d0d0d0"), ("-", "#ffa500"),
    ("0", "#d0d0d0"), (".", "#d0d0d0"), ("=", "#008000"), ("+", "#ffa500"),
    ("C", "#ff4500")
]

# Create and place the buttons
row_val = 1
col_val = 0
for label, color in button_data:
    button = tk.Button(root, text=label, font=("Helvetica", 16), padx=20, pady=20, width=2, bg=color)
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", click_button)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure rows and columns to expand with window resizing
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the GUI event loop
root.mainloop()
