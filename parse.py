#finding out the keywords from the user's description

# def keywords():

import string
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

#getting the user paragraph
user_paragraph = input("Hi! Welcome to Psychology Assistant. Please type a paragraph to let us know how you are feeling. Be as specific as you can!\n\n")
print("\n\nIs this how you are feeling?:\n",user_paragraph)

#turning input into smaller strings
all_words = user_paragraph.split()
items = len(all_words)
print(items)

#cleaning the input
stop_words = stopwords.words("english")
exclude = set(string.punctuation)

for i in (0,items-1):
	print(i)
	if all_words[i] in stop_words:
		all_words.remove(all_words[i])
	i=i+1



print(all_words)