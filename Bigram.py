import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import tqdm

nltk.download('punkt')

text = "This is an example of a bigram in Python"
tokens = word_tokenize(text)  # Tokenizing the text
bigrams = list(ngrams(tokens, 2))  # Creating bigrams

print(text)