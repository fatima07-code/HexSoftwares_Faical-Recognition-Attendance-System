import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, "database", "employees.db")

DATASET_PATH = os.path.join(BASE_DIR, "dataset")

TRAINER_PATH = os.path.join(BASE_DIR, "trainer")

ATTENDANCE_PATH = os.path.join(BASE_DIR, "attendance", "attendance.csv")

HAARCASCADE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "haarcascade_frontalface_default.xml"
)

IMAGE_COUNT = 30