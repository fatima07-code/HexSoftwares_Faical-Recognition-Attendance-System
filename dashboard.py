import tkinter as tk
from tkinter import messagebox

from register_employee import RegisterEmployee
from recognize_faces import FaceRecognition
from view_attendance import ViewAttendance
from PIL import Image, ImageTk
from ui_utils import set_background



class Dashboard:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Facial Recognition Attendance System")
        self.root.geometry("900x600")
        set_background(self.root, "assets/image1.jpeg", 900, 600)
        self.root.resizable(False, False)

        heading = tk.Label(
            self.root,
            text="Employee Attendance Dashboard",
            font=("Arial", 22, "bold")
        )
        heading.pack(pady=20)

        register_btn = tk.Button(
            self.root,
            text="Register Employee",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.open_register_employee
        )
        register_btn.pack(pady=10)

        train_btn = tk.Button(
            self.root,
            text="Model Info",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.train_faces
        )
        train_btn.pack(pady=10)

        recognize_btn = tk.Button(
            self.root,
            text="Recognize Face",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.open_recognition
        )
        recognize_btn.pack(pady=10)

        attendance_btn = tk.Button(
            self.root,
            text="Attendance Report",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.attendance_report
        )
        attendance_btn.pack(pady=10)

        exit_btn = tk.Button(
            self.root,
            text="Exit",
            font=("Arial", 12),
            width=25,
            height=2,
            bg="red",
            fg="white",
            command=self.root.destroy
        )
        exit_btn.pack(pady=20)

        self.root.mainloop()

   
    def open_register_employee(self):
        RegisterEmployee()

  
    def train_faces(self):
        messagebox.showinfo(
        "Information",
        "This system uses DeepFace pretrained model.\nNo training is required. Recognition works directly from dataset."
    )

   
    def open_recognition(self):
        FaceRecognition()

  
    def attendance_report(self):
        ViewAttendance()


if __name__ == "__main__":
    Dashboard()