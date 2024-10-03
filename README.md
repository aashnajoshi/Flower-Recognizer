# Flower-Recognizer
A deep learning model designed to classify flowers such as Rose, Sunflower, and Tulip using image inputs.

## Features
- Flower classification from user-provided images.
- Batch categorization of high-quality images for improved model performance.

## Usage
### Install required libraries:
```bash
pip install -r requirements.txt
```

### While to run the code:
```bash
python main.py
```

## Description of various files:
- **Analyzer.h5:** Pretrained model trained using [TeachableMachines](https://teachablemachine.withgoogle.com/) for flower classification. For now, the model is only trained to recognize 3 flowers i.e. __Rose, Sunflower, and Tulips__
- **app.py:** Contains a streamlit-based version of the main code. 
- **flower_sort.py:** Batches and categorizes images.
- **labels.txt:** Contains the labels for the flower categories.
- **main.py:** Recognizes flowers from the provided image.
- **requirements.txt:** Dependencies for the project.
