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
import re
import pandas as pd 
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


#load the master data sheet
data = list(csv.reader(open(pd.read_csv('keywords.txt'), mode="r+")))[1:]

#generate the labels or "answers"
answers = []
print(data[0])
for i in range(len(data)):
	votes = Counter([data[i][5], data[i][8], data[i][11]])
	print(votes)
	if votes["Yes"] >1:
		answers.append(1)
	else:
		answers.append(0)
answers = np.array(answers)

#time to clean the data
#process the text data
text = [point[1] for point in data]
stop_words = stopwords.words("english")
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
	stop_free = " ".join([i for i in doc.lower().split() if i not in stop_words])
	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
	normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
	return normalized

text = np.array([clean(point) for point in text])

#set up for training and testing
train_data, test_data, train_labels, test_labels = train_test_split(text,answers,test_size=.2)

#Code for vectorization
vectorizer = TfidfVectorizer()
vectorised_train_data = vectorizer.fit_transform(train_data)

#building the model
classifier = LinearSVC()
classifier.fit(vectorised_train_data, train_labels)

#processing test data
vectorised_test_data = vectorizer.transform(test_data)
predictions = classifier.predict(vectorised_test_data)

#getting metrics
accuracy = accuracy_score(test_labels, predictions)
precision = precision_score(test_labels, predictions, pos_label = 1)
recall = recall_score(test_labels, predictions, pos_label =1)
f1 = f1_score(test_labels, predictions, pos_label=1)

print(str(accuracy))
print(str(precision))
print(str(recall))
print(str(f1))

# actually testing it out

user_input = input('send me a message!\n')
user_data = np.array([user_input])
vectorised_user_data = vectorizer.transform(user_data)

while(user_input != 'quit'):
 prediction = classifier.predict(vectorised_user_data)
 print(prediction)
 user_input = input('Send me a message!\n')
 user_data = np.arrary([user_input])
 vectorised_user_data = vectorizer.transform(user_data)
print('Bye!')










