# Model trained using: https://teachablemachine.withgoogle.com/

from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tkinter import filedialog
import tkinter as tk
import time
import os

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model & labels
model = load_model("Analyzer.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

# Create the array to feed into the keras model where the 'length' or number of images you can put into the array is determined by the first position in the shape tuple.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

os.system('cls')

print("Hello, I am an Flower Classifier, currently i know only 3 flowers; Rose, Sunflower and Tulip, you can send me any image of these 3 flowers and i will try to detect them accurately!!")

time.sleep(5)

# Open a file dialog for the user to select a file
path = filedialog.askopenfilename(title="Select Image File")
image = Image.open(path).convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)