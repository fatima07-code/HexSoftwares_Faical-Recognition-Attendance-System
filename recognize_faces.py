import cv2
import os
import tempfile
import time
from deepface import DeepFace

from database import get_employee_by_id
from attendance import mark_attendance
from config import DATASET_PATH


class FaceRecognition:

    def __init__(self):
        self.start()

    def start(self):

        cap = cv2.VideoCapture(0)

        print("Live Face Recognition Started")
        print("Press ESC to Exit")

        last_recognition_time = 0
        last_employee_id = None

        name = "Unknown"
        dept = ""
        status = ""

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            current_time = time.time()

            # Run recognition every 2 seconds
            if current_time - last_recognition_time > 2:

                last_recognition_time = current_time

                temp = tempfile.NamedTemporaryFile(
                    suffix=".jpg",
                    delete=False
                )

                cv2.imwrite(temp.name, frame)

                try:
                    result = DeepFace.find(
                        img_path=temp.name,
                        db_path=DATASET_PATH,
                        enforce_detection=False,
                        silent=True
                    )

                    df = result[0]

                    if not df.empty:

                        identity = df.iloc[0]["identity"]

                        employee_id = os.path.basename(
                            os.path.dirname(identity)
                        )

                        employee = get_employee_by_id(employee_id)

                        if employee:

                            name = employee[2]
                            dept = employee[3]

                            marked = mark_attendance(
                                employee[1],
                                name,
                                dept
                            )

                            # ✅ POPUP ONLY ONCE PER EMPLOYEE
                            if employee_id != last_employee_id:

                                last_employee_id = employee_id

                                import tkinter as tk
                                from tkinter import messagebox

                                root = tk.Tk()
                                root.withdraw()

                                messagebox.showinfo(
                                    "Attendance System",
                                    "✔ Your attendance has been marked successfully"
                                )

                                root.destroy()

                            # status handling
                            if marked:
                                status = "PRESENT"
                            else:
                                status = "ALREADY MARKED"

                    else:
                        name = "Unknown"
                        dept = ""
                        status = ""

                except Exception as e:
                    print("Error:", e)
                    name = "Unknown"
                    dept = ""
                    status = ""

                os.remove(temp.name)

            # Draw UI on frame
            cv2.rectangle(frame, (20, 20), (350, 140), (0, 255, 0), 2)

            cv2.putText(frame, f"Name: {name}", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            if dept:
                cv2.putText(frame, f"Dept: {dept}", (30, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            if status:
                cv2.putText(frame, f"{status}", (30, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.imshow("Face Recognition System", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    def recognize(self, image_path):

        try:

            result = DeepFace.find(
                img_path=image_path,
                db_path=DATASET_PATH,
                enforce_detection=False,
                silent=True
            )

            df = result[0]

            if df.empty:
                print("❌ Unknown Person")
                return

            identity = df.iloc[0]["identity"]

            employee_id = os.path.basename(os.path.dirname(identity))

            employee = get_employee_by_id(employee_id)

            if not employee:
                print("❌ Employee not found")
                return

            name = employee[2]
            dept = employee[3]

            
            status = mark_attendance(employee[1], name, dept)

            if status:
                status_text = "✔ Present"
            else:
                status_text = "⚠ Already Marked"

            print(f"{name} recognized")

            

            img = cv2.imread(image_path)

            text1 = f"{name}"
            text2 = f"ID: {employee[1]}"
            text3 = f"{dept}"
            text4 = status_text

            cv2.rectangle(img, (20, 20), (400, 160), (0, 255, 0), 2)

            cv2.putText(img, text1, (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            cv2.putText(img, text2, (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            cv2.putText(img, text3, (30, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            cv2.putText(img, text4, (30, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow("Recognition Result", img)
            cv2.waitKey(2000)
            cv2.destroyWindow("Recognition Result")

        except Exception as e:
            print("Error:", e)