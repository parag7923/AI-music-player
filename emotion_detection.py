from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def get_emotion(text: str):
    results = emotion_classifier(text)
    
    return results[0]['label']
