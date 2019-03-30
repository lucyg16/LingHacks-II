import random
import csv
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC 
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import numpy as np
from collections import Counter
nltk.download("stopwords")
nltk.download("wordnet")

from nltk.corpus import wordnet as wn

# take out keywords from a user inputted text

# for each mental disorder, create a 'similarity score' based on the keywords
# calculate similarity between keyword against each symptom of mental disorder
# calculate overall similarity for mental disorder based on how many symptoms matched
# for each mental disorder:
#   for each keyword:
#       for each symptom:
#           how similar?
# calculate similarity score

# return mental disorder with the highest 'similarity score'
