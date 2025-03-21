import re

def detect_question(text):
    question_words = ["what", "why", "how", "when", "where", "who"]
    return any(re.search(rf"\b{word}\b", text.lower()) for word in question_words)