from deepface import DeepFace

print("Step 1")

result = DeepFace.find(
    img_path="dataset/201/201_1.jpg",
    db_path="dataset",
    enforce_detection=False,
    silent=True
)

print("Step 2")
print(result)