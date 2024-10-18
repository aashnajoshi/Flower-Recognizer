from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import streamlit as st

model = load_model("Analyzer.h5", compile=False)
class_names = open("labels.txt", "r").readlines()
np.set_printoptions(suppress=True)

st.title("Flower Classifier")

def classify_image():
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if image_file and st.button("Analyze Image"):
        st.write("Analyzing your image!")
        image = Image.open(image_file).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.LANCZOS)

        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()
        confidence_score = prediction[0][index]
        
        st.write("Analysis Successful!")
        st.write(f"Flower: {class_name[2:]}")
        st.write(f"Confidence Score: {confidence_score:.2f}")

st.write("I am a Flower Classifier!\nI know Rose, Sunflower, and Tulip.\nPlease select an image of one of these flowers.")
classify_image()