#the VADER sentiment intensity analyzer to analyze the sentiment of a given text

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the VADER sentiment intensity analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample text
text = "I hate this ugly product that has nothing to do with the world and everything in it"

# Analyze the sentiment of the text
sentiment_scores = analyzer.polarity_scores(text)

# Interpret the sentiment scores
compound_score = sentiment_scores['compound']

if compound_score >= 0.05:
    sentiment = "Positive"
elif compound_score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment analysis results
print("Text:", text)
print("Sentiment:", sentiment)
print("Sentiment Scores:", sentiment_scores)
