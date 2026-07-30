import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# Static Login Credentials
# ------------------------------_
users = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "librarian": {
        "password": "lib123",
        "role": "Librarian"
    },
    "member": {
        "password": "member123",
        "role": "Member"
    }
}

def logout(window):

    window.destroy()

    root.deiconify()
# -------------------------------
# Dashboard Window
# -------------------------------
def open_dashboard(role):

    dashboard = tk.Toplevel()

    dashboard.title("Library Management System")

    dashboard.geometry("700x450")

    dashboard.configure(bg="#F4F6F9")

    heading = tk.Label(
        dashboard,
        text="Library Management System",
        font=("Arial", 22, "bold"),
        bg="#F4F6F9",
        fg="#1F4E79"
    )

    heading.pack(pady=20)

    role_label = tk.Label(
        dashboard,
        text=f"Logged in as : {role}",
        font=("Arial", 16),
        bg="#F4F6F9"
    )

    role_label.pack(pady=10)

    info = tk.Label(
        dashboard,
        font=("Arial", 13),
        bg="#F4F6F9",
        fg="gray"
    )

    info.pack(pady=10)

    module_frame = tk.Frame(dashboard, bg="#F4F6F9")
    module_frame.pack(pady=25)

    buttons = [
        "Book Catalog",
        "Book Issue & Return",
        "Member Management",
        "Fine Calculation",
        "Dashboard / Reports"
    ]

    for text in buttons:

        tk.Button(
            module_frame,
            text=text,
            width=28,
            height=2,
            bg="#1F4E79",
            fg="white",
            font=("Arial", 11)
        ).pack(pady=6)

    tk.Button(
        dashboard,
        text="Logout",
        width=18,
        bg="red",
        fg="white",
       command=lambda: logout(dashboard)
    ).pack(pady=20)


# -------------------------------
# Login Function
# -------------------------------
def login():

    username = username_entry.get().strip().lower()

    password = password_entry.get().strip()

    role = role_box.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required.")
        return

    if username not in users:
        messagebox.showerror("Error", "Invalid Username")
        return

    if users[username]["password"] != password:
        messagebox.showerror("Error", "Incorrect Password")
        return

    if users[username]["role"] != role:
        messagebox.showerror("Error", "Selected Role is Incorrect")
        return
    messagebox.showinfo("Success", f"Welcome {role}")

    root.withdraw()        # Hide login window
    open_dashboard(role)
    

# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()

root.title("Library Login")

root.geometry("500x550")

root.configure(bg="#EAF2F8")


title = tk.Label(
    root,
    text="Library Management System",
    font=("Arial", 22, "bold"),
    bg="#EAF2F8",
    fg="#1F4E79"
)

title.pack(pady=25)


frame = tk.Frame(root, bg="white", bd=2, relief="ridge")

frame.pack(padx=35, pady=20, fill="both", expand=True)


tk.Label(
    frame,
    text="Login",
    font=("Arial", 18, "bold"),
    bg="white"
).pack(pady=20)


# Username
tk.Label(
    frame,
    text="Username",
    bg="white",
    font=("Arial", 11)
).pack(anchor="w", padx=40)

username_entry = ttk.Entry(frame, width=35)

username_entry.pack(pady=5)


# Password
tk.Label(
    frame,
    text="Password",
    bg="white",
    font=("Arial", 11)
).pack(anchor="w", padx=40)

password_entry = ttk.Entry(frame, show="*", width=35)

password_entry.pack(pady=5)


# Role
tk.Label(
    frame,
    text="Role",
    bg="white",
    font=("Arial", 11)
).pack(anchor="w", padx=40)

role_box = ttk.Combobox(
    frame,
    values=["Admin", "Librarian", "Member"],
    state="readonly",
    width=32
)

role_box.current(0)

role_box.pack(pady=5)


# Login Button
tk.Button(
    frame,
    text="Login",
    command=login,
    width=22,
    height=2,
    bg="#1F4E79",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=25)


# Demo Credentials
demo = tk.Label(
    frame,
    text=(
        "Demo Credentials\n\n"
        "Admin      : admin / admin123\n"
        "Librarian : librarian / lib123\n"
        "Member    : member / member123"
    ),
    justify="left",
    bg="white",
    fg="gray",
    font=("Arial", 10)
)

demo.pack(pady=10)


