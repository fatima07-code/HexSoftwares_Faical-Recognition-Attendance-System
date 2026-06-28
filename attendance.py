import csv
import os
from datetime import datetime

from config import ATTENDANCE_PATH


def mark_attendance(employee_id, name, department):

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    file_exists = os.path.exists(ATTENDANCE_PATH)

    # Create CSV if it doesn't exist
    if not file_exists:

        with open(ATTENDANCE_PATH, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Employee ID",
                "Name",
                "Department",
                "Date",
                "Time",
                "Status"
            ])

    # Prevent duplicate attendance
    with open(ATTENDANCE_PATH, "r", newline="") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0:

                if row[0] == employee_id and row[3] == today:

                    return False

    # Mark attendance
    with open(ATTENDANCE_PATH, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            employee_id,
            name,
            department,
            today,
            current_time,
            "Present"
        ])

    return True