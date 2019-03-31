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

#cleaning the input
stop_words = stopwords.words("english")
exclude = set(string.punctuation)

i=0
while (i < len(all_words)):
	print(i)
	if all_words[i] in stop_words:
		all_words.remove(all_words[i])
	else:
		i=i+1


# text = [point[1] for point in all_words]
# stop_words = stopwords.words("english")
# exclude = set(string.punctuation)

# def clean(doc):
# 	stop_free = " ".join([i for i in doc.lower().split() if i not in stop_words])
# 	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)

# text = np.array([clean(point) for point in text])




print(all_words)