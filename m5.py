import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("Fine Calculation")
root.geometry("700x600")
root.configure(bg="#F4F6F9")

title = tk.Label(
    root,
    text="Library Fine Calc",
    font=("Arial", 22, "bold"),
    bg="#F4F6F9",
    fg="#1F4E79"
)
title.pack(pady=20)

# -----------------------------
# Form Frame
# -----------------------------

frame = tk.LabelFrame(
    root,
    text="Fine Details",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=20
)

frame.pack(padx=20, pady=10, fill="both", expand=True)

# Book ID
tk.Label(frame, text="Book ID", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=8)

book_entry = ttk.Entry(frame, width=30)
book_entry.grid(row=0, column=1, pady=8)

# Member ID
tk.Label(frame, text="Member ID", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=8)

member_entry = ttk.Entry(frame, width=30)
member_entry.grid(row=1, column=1, pady=8)

# Due Date
tk.Label(frame, text="Due Date (DD-MM-YYYY)", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=8)

due_entry = ttk.Entry(frame, width=30)
due_entry.grid(row=2, column=1, pady=8)

# Return Date
tk.Label(frame, text="Return Date (DD-MM-YYYY)", font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=8)

return_entry = ttk.Entry(frame, width=30)
return_entry.grid(row=3, column=1, pady=8)

# -----------------------------
# Result Labels
# -----------------------------

late_label = tk.Label(
    frame,
    text="Late Days : 0",
    font=("Arial", 12, "bold"),
    fg="blue"
)

late_label.grid(row=5, column=0, columnspan=2, pady=10)

fine_label = tk.Label(
    frame,
    text="Fine Amount : ₹0",
    font=("Arial", 12, "bold"),
    fg="red"
)

fine_label.grid(row=6, column=0, columnspan=2, pady=10)

# -----------------------------
# Calculate Function
# -----------------------------

def calculate_fine():

    if (
        book_entry.get() == "" or
        member_entry.get() == "" or
        due_entry.get() == "" or
        return_entry.get() == ""
    ):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:

        due = datetime.strptime(
            due_entry.get(),
            "%d-%m-%Y"
        )

        returned = datetime.strptime(
            return_entry.get(),
            "%d-%m-%Y"
        )

    except:

        messagebox.showerror(
            "Error",
            "Date format should be DD-MM-YYYY."
        )

        return

    late_days = (returned - due).days

    if late_days < 0:
        late_days = 0

    fine = late_days * 10

    late_label.config(
        text=f"Late Days : {late_days}"
    )

    fine_label.config(
        text=f"Fine Amount : ₹{fine}"
    )

# -----------------------------
# Clear Function
# -----------------------------

def clear_fields():

    book_entry.delete(0, tk.END)
    member_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)
    return_entry.delete(0, tk.END)

    late_label.config(text="Late Days : 0")
    fine_label.config(text="Fine Amount : ₹0")

# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(frame)

button_frame.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=20
)

tk.Button(
    button_frame,
    text="Calculate Fine",
    width=18,
    bg="#1F4E79",
    fg="white",
    command=calculate_fine
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Clear",
    width=18,
    bg="gray",
    fg="white",
    command=clear_fields
).grid(row=0, column=1, padx=10)

root.mainloop()
