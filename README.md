## Requirements:
Python(3.8) **

## All required libraries can be installed using a single-line command:
```bash
  pip install -r requirements.txt 
```
## While to run the code:
```bash
  python main.py
```
## Description about various files:
- main.py: recognizes the flower from the image given to it by user
- flower_sort.py: to batch categorize high-quality images for better performance
- Analyzer.h5: Model trained using [TeachableMachines](https://teachablemachine.withgoogle.com/) to classify the flowers into categories. For now, the model is only trained to recognize 3 flowers i.e. __Rose, Sunflower, and Tulips__
