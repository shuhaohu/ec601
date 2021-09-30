# export GOOGLE_APPLICATION_CREDENTIALS="/media/sf_dropbox_ec602/ec602/pelagic-force-326821-5dc70bdbd2e9.json"
# First step is export the google credential in terminal.
# Imports the Google Cloud client library
from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"You are welcome This is a test about sentiment of the input text. "


document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment


print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

if sentiment.score > 0:
    print("This is a postive sentiment sentence ")
else:
    print("This is a negative sentiment sentence ")