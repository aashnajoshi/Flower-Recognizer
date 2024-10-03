from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tkinter import filedialog, Label, Button, Tk
import os

model = load_model("Analyzer.h5", compile=False)
class_names = open("labels.txt", "r").readlines()
np.set_printoptions(suppress=True)

root = Tk()
root.title("Flower Classifier")

def classify_image():
    path = filedialog.askopenfilename(title="Select Image File")
    if path:
        image = Image.open(path).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()
        confidence_score = prediction[0][index]
        result_label.config(text=f"Class: {class_name[2:]}\nConfidence Score: {confidence_score:.2f}")

welcome_label = Label(root, text="I am a Flower Classifier!\nI know Rose, Sunflower, and Tulip.\nPlease select an image of one of these flowers.", wraplength=300)
welcome_label.pack(pady=20)
classify_button = Button(root, text="Select Image & Classify", command=classify_image)
classify_button.pack(pady=10)
result_label = Label(root, text="", wraplength=300)
result_label.pack(pady=10)

root.geometry("400x300")
root.mainloop()
