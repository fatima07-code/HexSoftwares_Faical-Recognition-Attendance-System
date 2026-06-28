import tkinter as tk
from tkinter import messagebox
import os

from database import add_employee, employee_exists
from config import DATASET_PATH
from capture_faces import FaceCapture
from ui_utils import set_background


class RegisterEmployee:

    def __init__(self):

        self.window = tk.Toplevel()
        self.window.title("Register Employee")
        self.window.geometry("500x450")
        self.window.resizable(False, False)

        # ✅ FIXED: correct window reference + proper image size
        set_background(self.window, "assets/image1.jpeg", 500, 450)

        tk.Label(
            self.window,
            text="Register New Employee",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=20)

        tk.Label(self.window, text="Employee ID", bg="white").pack()

        self.emp_id = tk.Entry(self.window, width=30)
        self.emp_id.pack(pady=5)

        tk.Label(self.window, text="Employee Name", bg="white").pack()

        self.name = tk.Entry(self.window, width=30)
        self.name.pack(pady=5)

        tk.Label(self.window, text="Department", bg="white").pack()

        self.department = tk.Entry(self.window, width=30)
        self.department.pack(pady=5)

        tk.Button(
            self.window,
            text="Register",
            width=20,
            command=self.register
        ).pack(pady=20)

    def register(self):

        employee_id = self.emp_id.get().strip()
        name = self.name.get().strip()
        department = self.department.get().strip()

        if employee_id == "" or name == "" or department == "":

            messagebox.showwarning(
                "Missing Data",
                "Please fill all fields."
            )
            return

        if employee_exists(employee_id):

            messagebox.showerror(
                "Duplicate",
                "Employee ID already exists."
            )
            return

        add_employee(employee_id, name, department)

        folder = os.path.join(DATASET_PATH, employee_id)
        os.makedirs(folder, exist_ok=True)

        messagebox.showinfo(
            "Success",
            "Employee Registered Successfully.\nFace capture will now start."
        )

        FaceCapture(employee_id)

        self.window.destroy()