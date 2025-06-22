# review_checker/check_review.py

from transformers import pipeline

# Load pre-trained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

def check_review(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']

    # Simple interpretation
    if label == "NEGATIVE" and score > 0.9:
        return "⚠️ Likely FAKE or Manipulated Review", score
    elif label == "POSITIVE" and score < 0.6:
        return "⚠️ Possibly Overly Polished – Needs Review", score
    else:
        return "✅ Review seems Legit", score
