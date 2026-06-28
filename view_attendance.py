import tkinter as tk
from tkinter import ttk
import csv
import os

from config import ATTENDANCE_PATH


class ViewAttendance:

    def __init__(self):

        self.root = tk.Toplevel()

        self.root.title("Attendance Report")

        self.root.geometry("800x500")

        columns = (
            "Employee ID",
            "Name",
            "Department",
            "Date",
            "Time",
            "Status"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings"
        )

        for col in columns:

            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill="both", expand=True)

        self.load_data()

    def load_data(self):

        if not os.path.exists(ATTENDANCE_PATH):
            return

        with open(ATTENDANCE_PATH, "r", newline="") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                self.tree.insert("", tk.END, values=row)