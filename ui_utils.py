from PIL import Image, ImageTk
import tkinter as tk


def set_background(window, image_path, width, height):

    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)

    bg = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # IMPORTANT: prevent garbage collection
    label.image = bg

    return label