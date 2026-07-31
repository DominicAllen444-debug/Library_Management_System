import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Static Dashboard Data
# -----------------------------

total_books = 250
available_books = 180
issued_books = 70
total_members = 120
overdue_books = 8
fine_collected = 2450

# -----------------------------
# Window
# -----------------------------

root = tk.Tk()

root.title("Library Dashboard")

root.geometry("1200x700")

root.configure(bg="#F4F6F9")

# -----------------------------
# Heading
# -----------------------------

title = tk.Label(
    root,
    text="Library Management Dashboard",
    font=("Arial",22,"bold"),
    bg="#F4F6F9",
    fg="#1F4E79"
)

title.pack(pady=15)

# -----------------------------
# Card Function
# -----------------------------

def create_card(parent,title,value,color,column):

    frame = tk.Frame(
        parent,
        bg=color,
        width=170,
        height=90
    )

    frame.grid(row=0,column=column,padx=12)

    frame.grid_propagate(False)

    tk.Label(
        frame,
        text=title,
        bg=color,
        fg="white",
        font=("Arial",12,"bold")
    ).pack(pady=10)

    tk.Label(
        frame,
        text=str(value),
        bg=color,
        fg="white",
        font=("Arial",18,"bold")
    ).pack()

# -----------------------------
# Cards
# -----------------------------

card_frame = tk.Frame(root,bg="#F4F6F9")

card_frame.pack(pady=10)

create_card(card_frame,"Total Books",total_books,"#1F77B4",0)

create_card(card_frame,"Available",available_books,"green",1)

create_card(card_frame,"Issued",issued_books,"orange",2)

create_card(card_frame,"Members",total_members,"purple",3)

create_card(card_frame,"Overdue",overdue_books,"red",4)

create_card(card_frame,"Fine (₹)",fine_collected,"#009688",5)

# -----------------------------
# Main Content
# -----------------------------

main = tk.Frame(root,bg="#F4F6F9")

main.pack(fill="both",expand=True,padx=20,pady=20)

# -----------------------------
# Bar Chart
# -----------------------------

chart = tk.LabelFrame(
    main,
    text="Library Statistics",
    font=("Arial",12,"bold")
)

chart.pack(side="left",fill="both",expand=True,padx=10)

canvas = tk.Canvas(
    chart,
    width=500,
    height=350,
    bg="white"
)

canvas.pack(padx=10,pady=10)

values = [
    total_books,
    available_books,
    issued_books,
    total_members,
    overdue_books
]

labels = [
    "Books",
    "Available",
    "Issued",
    "Members",
    "Overdue"
]

colors = [
    "#1F77B4",
    "green",
    "orange",
    "purple",
    "red"
]

x = 40

for value,label,color in zip(values,labels,colors):

    height = value

    if height > 250:
        height = 250

    canvas.create_rectangle(
        x,
        300-height,
        x+50,
        300,
        fill=color
    )

    canvas.create_text(
        x+25,
        315,
        text=label
    )

    canvas.create_text(
        x+25,
        285-height,
        text=str(value)
    )

    x += 85

# -----------------------------
# Recent Activities
# -----------------------------

activity = tk.LabelFrame(
    main,
    text="Recent Activities",
    font=("Arial",12,"bold")
)

activity.pack(side="right",fill="both",expand=True,padx=10)

columns = (
    "Time",
    "Activity"
)

tree = ttk.Treeview(
    activity,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:

    tree.heading(col,text=col)

    tree.column(col,width=180)

tree.pack(padx=10,pady=10)

activities = [

("09:00","Book Issued"),

("09:30","New Member Added"),

("10:00","Book Returned"),

("10:45","Fine Calculated"),

("11:30","Book Issued"),

("12:00","Book Returned"),

("12:45","Member Updated"),

("01:15","Book Added"),

("02:00","Fine Paid"),

("03:10","Book Reserved")

]

for item in activities:

    tree.insert("",tk.END,values=item)

# -----------------------------
# Bottom Buttons
# -----------------------------

bottom = tk.Frame(root,bg="#F4F6F9")

bottom.pack(pady=10)

tk.Button(
    bottom,
    text="Refresh",
    width=15,
    bg="#1F4E79",
    fg="white",
    command=lambda:messagebox.showinfo(
        "Refresh",
        "Dashboard Updated."
    )
).grid(row=0,column=0,padx=10)

tk.Button(
    bottom,
    text="Logout",
    width=15,
    bg="red",
    fg="white",
    command=root.destroy
).grid(row=0,column=1,padx=10)

root.mainloop()
