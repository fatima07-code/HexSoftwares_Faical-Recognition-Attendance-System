import cv2
import os
import time
from config import DATASET_PATH, HAARCASCADE_PATH, IMAGE_COUNT


class FaceCapture:

    def __init__(self, employee_id):

        self.employee_id = employee_id

        self.folder = os.path.join(DATASET_PATH, employee_id)

        os.makedirs(self.folder, exist_ok=True)

        self.face_detector = cv2.CascadeClassifier(HAARCASCADE_PATH)

        self.capture_faces()

    def capture_faces(self):

        cap = cv2.VideoCapture(0)

        count = 0

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_detector.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5
            )

            for (x, y, w, h) in faces:

                face = frame[y:y+h, x:x+w]

                face = cv2.resize(face, (224, 224))

                count += 1
                time.sleep(0.5)

                image_path = os.path.join(
    self.folder,
    f"{self.employee_id}_{count}.jpg"
)

                cv2.imwrite(image_path, face)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x+w, y+h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Captured : {count}/{IMAGE_COUNT}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2
                )

                break

            cv2.imshow("Capturing Faces", frame)

            key = cv2.waitKey(1)

            if key == 27:
                break

            if count >= IMAGE_COUNT:
                break

        cap.release()

        cv2.destroyAllWindows()