# main.py

from review_checker.check_review import check_review

# Sample reviews
reviews = [
    "This is the best product I have ever used in my life. Highly recommended!!!",
    "Received completely wrong item. Total scam. Don't buy.",
    "It’s okay, not great. Arrived late but works fine."
]

for review in reviews:
    verdict, confidence = check_review(review)
    print(f"\nReview: {review}")
    print(f"Verdict: {verdict} (Confidence: {confidence:.2f})")
