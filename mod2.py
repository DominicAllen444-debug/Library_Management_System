
import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------
# Static Book Data
# ----------------------------
books = [
    {
        "Book ID": "B001",
        "Title": "Python Programming",
        "Author": "John Smith",
        "Genre": "Programming",
        "Publisher": "Tech Publications",
        "Year": "2022",
        "Status": "Available"
    },

    {
        "Book ID": "B002",
        "Title": "Database Systems",
        "Author": "Elmasri",
        "Genre": "Database",
        "Publisher": "Pearson",
        "Year": "2021",
        "Status": "Available"
    },

    {
        "Book ID": "B003",
        "Title": "Operating Systems",
        "Author": "Silberschatz",
        "Genre": "Computer Science",
        "Publisher": "McGraw Hill",
        "Year": "2020",
        "Status": "Issued"
    },

    {
        "Book ID": "B004",
        "Title": "Computer Networks",
        "Author": "Forouzan",
        "Genre": "Networking",
        "Publisher": "McGraw Hill",
        "Year": "2019",
        "Status": "Available"
    },

    {
        "Book ID": "B005",
        "Title": "Artificial Intelligence",
        "Author": "Russell",
        "Genre": "AI",
        "Publisher": "Pearson",
        "Year": "2023",
        "Status": "Available"
    },

    {
        "Book ID": "B006",
        "Title": "Software Engineering",
        "Author": "Pressman",
        "Genre": "Software",
        "Publisher": "McGraw Hill",
        "Year": "2022",
        "Status": "Available"
    }
]


# ----------------------------
# Main Window
# ----------------------------

root = tk.Tk()

root.title("Book Catalog System1")

root.geometry("1100x600")

root.configure(bg="#F4F6F9")


heading = tk.Label(
    root,
    text="Library Book Catalog",
    font=("Arial",22,"bold"),
    bg="#F4F6F9",
    fg="#1F4E79"
)

heading.pack(pady=15)


# ----------------------------
# Search Area
# ----------------------------

search_frame = tk.Frame(root,bg="#F4F6F9")

search_frame.pack()


search_entry = ttk.Entry(search_frame,width=35)

search_entry.grid(row=0,column=0,padx=10)


filter_box = ttk.Combobox(

    search_frame,

    values=["Title","Author","Genre"],

    state="readonly",

    width=20

)

filter_box.current(0)

filter_box.grid(row=0,column=1,padx=10)


# ----------------------------
# Table
# ----------------------------

columns = (

    "Book ID",

    "Title",

    "Author",

    "Genre",

    "Publisher",

    "Year",

    "Status"

)


tree = ttk.Treeview(

    root,

    columns=columns,

    show="headings",

    height=18

)


for col in columns:

    tree.heading(col,text=col)

    tree.column(col,width=140)


tree.pack(pady=20)


# ----------------------------
# Load Data
# ----------------------------

def load_books(book_list):

    tree.delete(*tree.get_children())

    for book in book_list:

        tree.insert(

            "",

            tk.END,

            values=(

                book["Book ID"],

                book["Title"],

                book["Author"],

                book["Genre"],

                book["Publisher"],

                book["Year"],

                book["Status"]

            )

        )


load_books(books)


# ----------------------------
# Search Function
# ----------------------------

def search_books():

    keyword = search_entry.get().lower()

    option = filter_box.get()

    result=[]

    for book in books:

        if keyword in book[option].lower():

            result.append(book)

    load_books(result)


# ----------------------------
# Reset Function
# ----------------------------

def reset_table():

    search_entry.delete(0,tk.END)

    filter_box.current(0)

    load_books(books)


# ----------------------------
# Book Details
# ----------------------------

def view_details():

    selected = tree.focus()

    if selected=="":

        messagebox.showwarning(

            "Warning",

            "Please select a book."

        )

        return

    values = tree.item(selected,"values")

    detail = tk.Toplevel()

    detail.title("Book Details")

    detail.geometry("420x350")

    detail.configure(bg="white")

    tk.Label(

        detail,

        text="Book Information",

        font=("Arial",18,"bold"),

        bg="white",

        fg="#1F4E79"

    ).pack(pady=15)

    labels = [

        "Book ID",

        "Title",

        "Author",

        "Genre",

        "Publisher",

        "Year",

        "Status"

    ]

    for i in range(len(labels)):

        tk.Label(

            detail,

            text=f"{labels[i]} : {values[i]}",

            bg="white",

            anchor="w",

            font=("Arial",11)

        ).pack(fill="x",padx=20,pady=4)


# ----------------------------
# Buttons
# ----------------------------

button_frame = tk.Frame(root,bg="#F4F6F9")

button_frame.pack()


tk.Button(

    button_frame,

    text="Search",

    width=15,

    bg="#1F4E79",

    fg="white",

    command=search_books

).grid(row=0,column=0,padx=8)


tk.Button(

    button_frame,

    text="Reset",

    width=15,

    bg="green",

    fg="white",

    command=reset_table

).grid(row=0,column=1,padx=8)


tk.Button(

    button_frame,

    text="View Details",

    width=15,

    bg="orange",

    fg="white",

    command=view_details

).grid(row=0,column=2,padx=8)


root.mainloop()

import subprocess

subprocess.Popen([
    "pythonw",
    r"C:\Users\harsh\Downloads\mod2.py"
])
