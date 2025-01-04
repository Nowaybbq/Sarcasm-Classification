from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import string

class SarcasmClassification:
    def __init__(self):
        # Tokenizer and Model determination
        self.model_path = "helinivan/english-sarcasm-detector"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path)

    def preprocess_data(self, text: str) -> str:
        # Text processing
        return text.lower().translate(str.maketrans("", "", string.punctuation)).strip()

    def classify(self, text: str):
        # Text classification
        processed_text = self.preprocess_data(text)
        tokenized_text = self.tokenizer(
            [processed_text], 
            padding=True, 
            truncation=True, 
            max_length=256, 
            return_tensors="pt"
        )
        output = self.model(**tokenized_text)
        probs = output.logits.softmax(dim=-1).tolist()[0]
        confidence = max(probs)
        prediction = probs.index(confidence)
        
        # Result evaluation
        if prediction == 1:
            label = "Sarcasm"
        else:
            label = "Normal Text"
        
        return {"label": label, "confidence": confidence}
