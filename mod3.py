import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

# =====================================================

# =====================================================

root = tk.Tk()
root.title("Library Management System - Book Issue & Return")
root.geometry("1300x700")
root.configure(bg="#F4F6F9")

# =====================================================
# STATIC DATA
# =====================================================

members = [
    "Rahul",
    "Priya",
    "Arun",
    "Sneha",
    "Karthik",
    "Anitha"
]

books = [
    "Python Programming",
    "Database Systems",
    "Operating Systems",
    "Computer Networks",
    "Artificial Intelligence",
    "Software Engineering",
    "Machine Learning"
]

issued_books = []

# =====================================================
# TITLE
# =====================================================

title = tk.Label(
    root,
    text="Book Issue & Return",
    font=("Arial", 22, "bold"),
    bg="#F4F6F9",
    fg="#1F4E79"
)
title.pack(pady=10)

# =====================================================
# LEFT FRAME
# =====================================================

left = tk.LabelFrame(
    root,
    text="Issue / Return Book",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=15
)

left.place(x=20, y=60, width=330, height=620)

# ---------------- MEMBER ----------------

tk.Label(left, text="Member Name").pack(anchor="w")

member_box = ttk.Combobox(
    left,
    values=members,
    state="readonly",
    width=35
)
member_box.pack(pady=5)

# ---------------- BOOK ----------------

tk.Label(left, text="Book Name").pack(anchor="w")

book_box = ttk.Combobox(
    left,
    values=books,
    state="readonly",
    width=35
)
book_box.pack(pady=5)

# ---------------- ISSUE DATE ----------------

tk.Label(left, text="Issue Date").pack(anchor="w")

issue_entry = ttk.Entry(left, width=38)
issue_entry.pack(pady=5)

# ---------------- DUE DATE ----------------

tk.Label(left, text="Due Date").pack(anchor="w")

due_entry = ttk.Entry(left, width=38)
due_entry.pack(pady=5)

today = datetime.today()

issue_entry.insert(
    0,
    today.strftime("%d-%m-%Y")
)

due_entry.insert(
    0,
    (today + timedelta(days=14)).strftime("%d-%m-%Y")
)

# ---------------- RETURN DATE ----------------

tk.Label(left, text="Return Date").pack(anchor="w")

return_entry = ttk.Entry(left, width=38)
return_entry.pack(pady=5)
# =====================================================
# BUTTONS
# =====================================================

issue_btn = tk.Button(
    left,
    text="Issue Book",
    width=20,
    bg="#1F4E79",
    fg="white"
)
issue_btn.pack(pady=8)

return_btn = tk.Button(
    left,
    text="Return Book",
    width=20,
    bg="darkgreen",
    fg="white"
)
return_btn.pack(pady=8)

clear_btn = tk.Button(
    left,
    text="Clear",
    width=20,
    bg="gray",
    fg="white"
)
clear_btn.pack(pady=8)

# =====================================================
# RIGHT FRAME
# =====================================================

right = tk.Frame(root, bg="#F4F6F9")
right.place(x=370, y=60, width=900, height=620)

# =====================================================
# SEARCH BAR
# =====================================================

search_frame = tk.Frame(right, bg="#F4F6F9")
search_frame.pack(fill="x", pady=5)

tk.Label(
    search_frame,
    text="Search :",
    bg="#F4F6F9",
    font=("Arial",10,"bold")
).pack(side="left")

search_entry = ttk.Entry(
    search_frame,
    width=35
)
search_entry.pack(side="left", padx=10)

search_btn = tk.Button(
    search_frame,
    text="Search",
    width=12,
    bg="#1F4E79",
    fg="white"
)
search_btn.pack(side="left")

reset_btn = tk.Button(
    search_frame,
    text="Reset",
    width=12,
    bg="green",
    fg="white"
)
reset_btn.pack(side="left", padx=5)

# =====================================================
# TABLE
# =====================================================

columns = (
    "Member",
    "Book",
    "Issue Date",
    "Due Date",
    "Return Date",
    "Fine",
    "Status"
)

tree = ttk.Treeview(
    right,
    columns=columns,
    show="headings",
    height=24,
    selectmode="browse"
)

widths = [120,180,100,100,100,70,90]

for col, w in zip(columns, widths):
    tree.heading(col, text=col)
    tree.column(col, width=w, anchor="center")

scroll = ttk.Scrollbar(
    right,
    orient="vertical",
    command=tree.yview
)

tree.configure(
    yscrollcommand=scroll.set
)

tree.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

# =====================================================
# LOAD TABLE
# =====================================================

def load_table():

    tree.delete(*tree.get_children())

    for item in issued_books:

        tree.insert(
            "",
            tk.END,
            values=(
                item["Member"],
                item["Book"],
                item["Issue Date"],
                item["Due Date"],
                item["Return Date"],
                f"₹{item['Fine']}",
                item["Status"]
            )
        )

# =====================================================
# CLEAR FORM
# =====================================================

def clear_fields():

    member_box.set("")
    book_box.set("")

    issue_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)
    return_entry.delete(0, tk.END)

    today = datetime.today()

    issue_entry.insert(
        0,
        today.strftime("%d-%m-%Y")
    )

    due_entry.insert(
        0,
        (today + timedelta(days=14)).strftime("%d-%m-%Y")
    )

clear_btn.config(command=clear_fields)


# =====================================================
# ISSUE BOOK
# =====================================================

def issue_book():

    member = member_box.get().strip()
    book = book_box.get().strip()
    issue_date = issue_entry.get().strip()
    due_date = due_entry.get().strip()

    # Validation

    if member == "" or book == "":
        messagebox.showerror(
            "Error",
            "Please select Member and Book."
        )
        return

    # Date validation

    try:
        datetime.strptime(issue_date, "%d-%m-%Y")
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        messagebox.showerror(
            "Error",
            "Invalid date format.\nUse DD-MM-YYYY."
        )
        return

    # Duplicate issue check

    for item in issued_books:

        if item["Book"] == book and item["Status"] == "Issued":
            messagebox.showwarning(
                "Warning",
                "This book is already issued."
            )
            return

    # Add new issued book

    issued_books.append({

        "Member": member,

        "Book": book,

        "Issue Date": issue_date,

        "Due Date": due_date,

        "Return Date": "-",

        "Fine": 0,

        "Status": "Issued"

    })

    load_table()

    clear_fields()

    messagebox.showinfo(
        "Success",
        "Book Issued Successfully."
    )


issue_btn.config(command=issue_book)


# =====================================================
# INITIAL TABLE LOAD
# =====================================================

load_table()

# =====================================================
# RETURN BOOK
# =====================================================

def return_book():

    member = member_box.get().strip()
    book = book_box.get().strip()
    return_date = return_entry.get().strip()

    if member == "" or book == "" or return_date == "":
        messagebox.showerror(
            "Error",
            "Please select Member, Book and Return Date."
        )
        return

    try:
        return_dt = datetime.strptime(return_date, "%d-%m-%Y")
    except ValueError:
        messagebox.showerror(
            "Error",
            "Return Date must be in DD-MM-YYYY format."
        )
        return

    for item in issued_books:

        if (item["Member"] == member and
            item["Book"] == book and
            item["Status"] == "Issued"):

            due_dt = datetime.strptime(
                item["Due Date"],
                "%d-%m-%Y"
            )

            late_days = (return_dt - due_dt).days

            if late_days < 0:
                late_days = 0

            fine = late_days * 5

            item["Return Date"] = return_date
            item["Fine"] = fine
            item["Status"] = "Returned"

            load_table()

            messagebox.showinfo(
                "Success",
                f"""Book Returned Successfully!

Late Days : {late_days}

Fine : ₹{fine}"""
            )

            clear_fields()

            return

    messagebox.showwarning(
        "Warning",
        "No issued record found."
    )
return_btn.config(command=return_book)
# =====================================================
# SEARCH BOOK
# =====================================================

def search_book():

    keyword = search_entry.get().strip().lower()

    tree.delete(*tree.get_children())

    for item in issued_books:

        if (keyword in item["Member"].lower() or
            keyword in item["Book"].lower() or
            keyword in item["Status"].lower()):

            tree.insert(
                "",
                tk.END,
                values=(
                    item["Member"],
                    item["Book"],
                    item["Issue Date"],
                    item["Due Date"],
                    item["Return Date"],
                    f"₹{item['Fine']}",
                    item["Status"]
                )
            )

search_btn.config(command=search_book)

# =====================================================
# RESET TABLE
# =====================================================

def reset_table():

    search_entry.delete(0, tk.END)

    load_table()

reset_btn.config(command=reset_table)

# =====================================================
# STATISTICS
# =====================================================

stats_label = tk.Label(
    right,
    text="",
    font=("Arial", 11, "bold"),
    bg="#F4F6F9",
    fg="#1F4E79"
)

stats_label.pack(pady=8)

def update_stats():

    total = len(issued_books)

    issued = sum(
        1 for item in issued_books
        if item["Status"] == "Issued"
    )

    returned = sum(
        1 for item in issued_books
        if item["Status"] == "Returned"
    )

    total_fine = sum(
        item["Fine"] for item in issued_books
    )

    stats_label.config(
        text=f"Total Books : {total}     "
             f"Issued : {issued}     "
             f"Returned : {returned}     "
             f"Fine Collected : ₹{total_fine}"
    )

# =====================================================
# UPDATE LOAD TABLE
# =====================================================

def load_table():

    tree.delete(*tree.get_children())

    for item in issued_books:

        tree.insert(
            "",
            tk.END,
            values=(
                item["Member"],
                item["Book"],
                item["Issue Date"],
                item["Due Date"],
                item["Return Date"],
                f"₹{item['Fine']}",
                item["Status"]
            )
        )

    update_stats()

load_table()

# =====================================================
# MAIN LOOP
# =====================================================

root.mainloop()
