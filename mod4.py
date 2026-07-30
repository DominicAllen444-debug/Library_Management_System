import tkinter as tk
from tkinter import ttk, messagebox


# -----------------------------------------
# Static Member Data
# -----------------------------------------

members = [

    {
        "ID": "M001",
        "Name": "Rahul Sharma",
        "Department": "CSE",
        "Phone": "9876543210",
        "Email": "rahul@gmail.com",
        "Membership": "Student",
        "Status": "Active"
    },

    {
        "ID": "M002",
        "Name": "Priya Kumar",
        "Department": "IT",
        "Phone": "9876501234",
        "Email": "priya@gmail.com",
        "Membership": "Faculty",
        "Status": "Active"
    },

    {
        "ID": "M003",
        "Name": "Arun",
        "Department": "ECE",
        "Phone": "9988776655",
        "Email": "arun@gmail.com",
        "Membership": "Student",
        "Status": "Inactive"
    }
]


# -----------------------------------------
# Main Window
# -----------------------------------------

root = tk.Tk()

root.title("Member Management")

root.geometry("1200x650")

root.configure(bg="#F4F6F9")


# -----------------------------------------
# Heading
# -----------------------------------------

title = tk.Label(
    root,
    text="Library Member Management",
    font=("Arial",22,"bold"),
    bg="#F4F6F9",
    fg="#1F4E79"
)

title.pack(pady=15)



# -----------------------------------------
# Left Form
# -----------------------------------------

form = tk.LabelFrame(
    root,
    text="Member Details",
    font=("Arial",12,"bold"),
    padx=20,
    pady=15
)

form.place(
    x=20,
    y=70,
    width=360,
    height=540
)



def create_label(text,row):

    tk.Label(
        form,
        text=text,
        font=("Arial",10)
    ).grid(
        row=row,
        column=0,
        sticky="w",
        pady=6
    )


create_label("Member ID",0)

id_entry = ttk.Entry(form,width=30)

id_entry.grid(row=0,column=1)


create_label("Name",1)

name_entry = ttk.Entry(form,width=30)

name_entry.grid(row=1,column=1)


create_label("Department",2)

dept_entry = ttk.Entry(form,width=30)

dept_entry.grid(row=2,column=1)


create_label("Phone",3)

phone_entry = ttk.Entry(form,width=30)

phone_entry.grid(row=3,column=1)


create_label("Email",4)

email_entry = ttk.Entry(form,width=30)

email_entry.grid(row=4,column=1)


create_label("Membership",5)

membership_box = ttk.Combobox(
    form,
    values=[
        "Student",
        "Faculty",
        "Staff"
    ],
    state="readonly",
    width=27
)

membership_box.current(0)

membership_box.grid(row=5,column=1)


create_label("Status",6)

status_box = ttk.Combobox(
    form,
    values=[
        "Active",
        "Inactive"
    ],
    state="readonly",
    width=27
)

status_box.current(0)

status_box.grid(row=6,column=1)



# -----------------------------------------
# Table
# -----------------------------------------

right = tk.Frame(
    root,
    bg="#F4F6F9"
)

right.place(
    x=410,
    y=70,
    width=760,
    height=540
)



# Search

search_frame=tk.Frame(right)

search_frame.pack(pady=5)


tk.Label(
    search_frame,
    text="Search Member"
).pack(side="left")


search_entry=ttk.Entry(
    search_frame,
    width=30
)

search_entry.pack(
    side="left",
    padx=10
)



# Table

columns=(

"ID",
"Name",
"Department",
"Phone",
"Email",
"Membership",
"Status"

)


tree=ttk.Treeview(
    right,
    columns=columns,
    show="headings",
    height=18
)


for col in columns:

    tree.heading(
        col,
        text=col
    )

    tree.column(
        col,
        width=100
    )


tree.pack(
    pady=15
)



# -----------------------------------------
# Load Table
# -----------------------------------------

def load_members(data=members):

    tree.delete(
        *tree.get_children()
    )


    for member in data:

        tree.insert(
            "",
            tk.END,
            values=(

                member["ID"],
                member["Name"],
                member["Department"],
                member["Phone"],
                member["Email"],
                member["Membership"],
                member["Status"]

            )
        )


load_members()



# -----------------------------------------
# Clear Fields
# -----------------------------------------

def clear_fields():

    id_entry.delete(0,tk.END)

    name_entry.delete(0,tk.END)

    dept_entry.delete(0,tk.END)

    phone_entry.delete(0,tk.END)

    email_entry.delete(0,tk.END)

    membership_box.current(0)

    status_box.current(0)



# -----------------------------------------
# Add Member
# -----------------------------------------

def add_member():

    if (
        id_entry.get()=="" or
        name_entry.get()=="" or
        dept_entry.get()=="" or
        phone_entry.get()=="" or
        email_entry.get()==""
    ):

        messagebox.showerror(
            "Error",
            "All fields are required"
        )

        return


    for m in members:

        if m["ID"]==id_entry.get():

            messagebox.showerror(
                "Error",
                "Member ID already exists"
            )

            return



    members.append({

        "ID":id_entry.get(),
        "Name":name_entry.get(),
        "Department":dept_entry.get(),
        "Phone":phone_entry.get(),
        "Email":email_entry.get(),
        "Membership":membership_box.get(),
        "Status":status_box.get()

    })


    load_members()

    clear_fields()


    messagebox.showinfo(
        "Success",
        "Member Added"
    )



# -----------------------------------------
# Select Row
# -----------------------------------------

def select_member(event):

    selected=tree.focus()


    if selected=="":

        return


    values=tree.item(
        selected,
        "values"
    )


    clear_fields()


    id_entry.insert(0,values[0])

    name_entry.insert(0,values[1])

    dept_entry.insert(0,values[2])

    phone_entry.insert(0,values[3])

    email_entry.insert(0,values[4])

    membership_box.set(values[5])

    status_box.set(values[6])



tree.bind(
    "<<TreeviewSelect>>",
    select_member
)



# -----------------------------------------
# Update Member
# -----------------------------------------

def update_member():

    selected=tree.focus()


    if selected=="":

        messagebox.showwarning(
            "Warning",
            "Select a member"
        )

        return


    index=tree.index(selected)


    members[index]={

        "ID":id_entry.get(),
        "Name":name_entry.get(),
        "Department":dept_entry.get(),
        "Phone":phone_entry.get(),
        "Email":email_entry.get(),
        "Membership":membership_box.get(),
        "Status":status_box.get()

    }


    load_members()

    clear_fields()


    messagebox.showinfo(
        "Updated",
        "Member Updated"
    )



# -----------------------------------------
# Delete Member
# -----------------------------------------

def delete_member():

    selected=tree.focus()


    if selected=="":

        messagebox.showwarning(
            "Warning",
            "Select member"
        )

        return


    index=tree.index(selected)


    members.pop(index)


    load_members()

    clear_fields()


    messagebox.showinfo(
        "Deleted",
        "Member Deleted"
    )



# -----------------------------------------
# Search
# -----------------------------------------

def search_member():

    keyword=search_entry.get().lower()


    result=[]


    for m in members:

        if (

            keyword in m["ID"].lower()
            or keyword in m["Name"].lower()
            or keyword in m["Department"].lower()

        ):

            result.append(m)



    load_members(result)



# -----------------------------------------
# Buttons
# -----------------------------------------

button_frame=tk.Frame(form)

button_frame.grid(
    row=8,
    column=0,
    columnspan=2,
    pady=25
)


tk.Button(
    button_frame,
    text="Add",
    width=10,
    bg="#1F4E79",
    fg="white",
    command=add_member
).grid(row=0,column=0,padx=5)



tk.Button(
    button_frame,
    text="Update",
    width=10,
    bg="green",
    fg="white",
    command=update_member
).grid(row=0,column=1,padx=5)



tk.Button(
    button_frame,
    text="Delete",
    width=10,
    bg="red",
    fg="white",
    command=delete_member
).grid(row=1,column=0,padx=5)



tk.Button(
    button_frame,
    text="Clear",
    width=10,
    bg="gray",
    fg="white",
    command=clear_fields
).grid(row=1,column=1,padx=5)



tk.Button(
    search_frame,
    text="Search",
    bg="#1F4E79",
    fg="white",
    command=search_member
).pack(side="left")



# -----------------------------------------
# Run
# -----------------------------------------

root.mainloop()