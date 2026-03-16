from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Sentiment Pro Day 7")

# We use a smaller model for the first run to keep things light
print("Loading model... please wait.")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class SentimentRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is online and storage is safe!"}

@app.post("/predict")
def predict(request: SentimentRequest):
    result = classifier(request.text)[0]
    return {"text": request.text, "label": result['label'], "score": round(result['score'], 4)}
