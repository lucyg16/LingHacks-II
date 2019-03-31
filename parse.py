#finding out the keywords from the user's description

# def keywords():

import string
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# #getting the user paragraph
# user_paragraph = input("Hi! Welcome to Psychology Assistant. Please type a paragraph to let us know how you are feeling. Be as specific as you can!\n\n")
# print("\n\nIs this how you are feeling?:\n",user_paragraph)

user_paragraph = "me sad. lonely, need friends."

#turning input into smaller strings
all_words = user_paragraph.split()

#cleaning the input
stop_words = stopwords.words('english')
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(array):
   stop_free = " ".join([i for i in array if i not in stop_words])
   punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
   normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
   return normalized.split(" ")

text = clean(all_words)

print(text)
