# News Article Text Summarizer
# Created by [Your Name]

import re
import heapq
import nltk
from nltk.corpus import stopwords

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Load the text file
with open("articles/sample_article.txt", 'r', encoding='utf-8') as file:
    text = file.read()

# Clean the text
text = re.sub(r'\s+', ' ', text)

# Tokenize sentences
sentences = nltk.sent_tokenize(text)

# Tokenize words and remove stopwords
stop_words = set(stopwords.words('english'))
word_frequencies = {}

for word in nltk.word_tokenize(text.lower()):
    if word not in stop_words and word.isalnum():
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

# Calculate weighted frequencies
maximum_freq = max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word] = word_frequencies[word] / maximum_freq

# Score sentences
sentence_scores = {}
for sent in sentences:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies:
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

# Select top 5 sentences as summary
summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)

# Output the summary
print("\nSummary:\n")
print(summary)
