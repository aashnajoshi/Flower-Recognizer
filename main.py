from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tkinter import filedialog
import tkinter as tk
import time
import os

root = tk.Tk()
root.withdraw()
np.set_printoptions(suppress=True)

model = load_model("Analyzer.h5", compile=False)
class_names = open("labels.txt", "r").readlines()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

os.system('cls' if os.name == 'nt' else 'clear')
print("Hello, I am a Flower Classifier! I know only 3 flowers: Rose, Sunflower, and Tulip. You can send me any image of these flowers, and I will try to detect them accurately!")

time.sleep(2)

path = filedialog.askopenfilename(title="Select Image File")
if not path:
    print("No file selected. Exiting...")
    exit()

image = Image.open(path).convert("RGB")
size = (224, 224)
image = ImageOps.fit(image, size, Image.LANCZOS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
data[0] = normalized_image_array
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index].strip()
confidence_score = prediction[0][index]

print("\nAnalysis Successful!")
print("Flower:", class_name[2:])
print(f"Confidence Score: {confidence_score:.2f}")