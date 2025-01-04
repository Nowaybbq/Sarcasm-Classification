from fastapi import FastAPI
from pydantic import BaseModel
from models.model import SarcasmClassification

app = FastAPI()
class TextInput(BaseModel):
    text:str

classifier = SarcasmClassification()

@app.post("/classify-text/")
def classify_text(input_data: TextInput):
    classification = classifier.classify(input_data.text)
    return {"text": input_data.text, "classification": classification}