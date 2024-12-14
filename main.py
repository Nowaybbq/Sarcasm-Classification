from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
# Input data
class TextInput(BaseModel):
    text:str

class sarcasmClassification:
    def __init__(self):
# Model initialization
        self.model = pipeline("text-classification", model="bert-base-uncased")

    def classify(self, text: str):
# Text classification 'Sarcasm' or 'Normal Text method'
        result = self.model(text)[0]
        label = result['label']
        if label == "LABEL_1":
            return "Sarcasm"
        elif label == "LABEL_0":
            return "Normal Text"

classifier = sarcasmClassification()

@app.post("/classify-text/")
def classify_text(input_data: TextInput):
    classification = classifier.classify(input_data.text)
    return {"text": input_data.text, "classification": classification}