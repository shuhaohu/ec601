# Imports the Google Cloud client library
from google.cloud import language_v1
import os

# Instantiates a client
client = language_v1.LanguageServiceClient()

def analyze_sentiment(text):
    textinput = text
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    output = [sentiment.score, sentiment.magnitude]
    return output