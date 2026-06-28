import tkinter as tk
from tkinter import messagebox
from dashboard import Dashboard
from ui_utils import set_background
USERNAME = "admin"
PASSWORD = "admin123"


class LoginWindow:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Employee Attendance System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.root.geometry("900x600")

        set_background(self.root, "assets/image1.jpeg", 900, 600)
        title = tk.Label(
            self.root,
            text="Facial Recognition Attendance System",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=20)

        tk.Label(self.root, text="Username", font=("Arial", 12)).pack()

        self.username = tk.Entry(self.root, font=("Arial", 12))
        self.username.pack(pady=5)

        tk.Label(self.root, text="Password", font=("Arial", 12)).pack()

        self.password = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.password.pack(pady=5)

        self.show_var = tk.BooleanVar()

        show_password = tk.Checkbutton(
            self.root,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password
        )

        show_password.pack()

        login_btn = tk.Button(
            self.root,
            text="Login",
            width=20,
            command=self.login
        )

        login_btn.pack(pady=20)

        exit_btn = tk.Button(
            self.root,
            text="Exit",
            width=20,
            bg="red",
            fg="white",
            command=self.root.destroy
        )

        exit_btn.pack()

        self.root.mainloop()

    def toggle_password(self):

        if self.show_var.get():
            self.password.config(show="")
        else:
            self.password.config(show="*")

    def login(self):

        user = self.username.get()
        pwd = self.password.get()

        if user == USERNAME and pwd == PASSWORD:

            self.root.destroy()

            Dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )