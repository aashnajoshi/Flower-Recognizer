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
os.system('cls')
print("Hello, I am an Flower Classifier, currently i know only 3 flowers; Rose, Sunflower and Tulip, you can send me any image of these 3 flowers and i will try to detect them accurately!!")

time.sleep(5)
path = filedialog.askopenfilename(title="Select Image File")
image = Image.open(path).convert("RGB")
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
data[0] = normalized_image_array

prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)
