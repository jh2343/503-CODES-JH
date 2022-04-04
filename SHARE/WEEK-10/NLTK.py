
#DEPENDANCIES
#conda install -c anaconda nltk
#inside python run: 
#import nltk; 
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('stopwords')
# nltk.download([
#     "names",
#     "stopwords",
#     "state_union",
#     "twitter_samples",
#     "movie_reviews",
#     "averaged_perceptron_tagger",
#     "vader_lexicon",
#     "punkt",
# ])

import nltk
import string 
from nltk.corpus import wordnet



print("-----------------------------")
print("EXAMPLE: VADAR SENTIMENT COMPUTE")
print("-----------------------------")
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
text="I love NLTK, its a great library"
score=sia.polarity_scores(text)
print('TEXT:',text)
print("SCORE:",score)


print("-----------------------------")
print("EXAMPLE: CHANGE CASE")
print("-----------------------------")
text = "The universe is Great! I won a lottery."
print(text.upper())
print(text.lower())


print("-----------------------------")
print("EXAMPLE: SENTANCE SEMENTATION")
print("-----------------------------")
text = "The universe is Great! I won a lottery."
print(nltk.tokenize.sent_tokenize(text))
Output: ['The universe is Great!', 'I won a lottery ']
print(text)

#
print("\n-----------------------------")
print("EXAMPLE: KEEP ONLY PRINTABLE CHAR")
print("-----------------------------")
s = "some\x00string. with\x15 funny characters"
print(s)
printable = set(string.printable); tmp=''
for char in s:
	if(char in printable): tmp=tmp+char
print(tmp)


print("\n-----------------------------")
print("EXAMPLE: REMOVE NEW LINES")
print("-----------------------------")
str1 = "\n line-1: Starbucks has the best coffee \n line-2: This is more text"
print(str1)
newstr = str1.splitlines()
print(newstr)

print("\n-----------------------------")
print("EXAMPLE: WORD TOKENIZE")
print("-----------------------------")
from nltk.tokenize import word_tokenize
s = '''Good muffins cost $3.88\nin New York.  Please buy me
... two of them.\n\nThanks.'''
print(word_tokenize(s))

print("\n-----------------------------")
print("EXAMPLE: LEMITIZATION")
print("-----------------------------")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))


print("\n-----------------------------")
print("EXAMPLE: STOPWORDS")
print("-----------------------------") 
from nltk.corpus import stopwords
print(stopwords.words('english'))


print("\n-----------------------------")
print("EXAMPLE: SEARCHING TEXT")
print("-----------------------------")
text = "line-1: Starbucks has the best coffee \n line-2: This is more text"
text = word_tokenize(text)
text = nltk.Text(text)
print(text.concordance("has"))


print("\n-----------------------------")
print("EXAMPLE: PARTS OF SPEECH (POS)")
print("-----------------------------")
text = "line-1: Starbucks has the best coffee \n line-2: This is more text"
text = nltk.word_tokenize(text)
print(text)
text = nltk.pos_tag(text)
print(text)


print("\n-----------------------------")
print("EXAMPLE: SYNONYMS,HYPERNYMS, AND ANTONYMS")
print("-----------------------------")
original_word='testing'
# original_word=lemmatizer.lemmatize(original_word)
synonyms = []
antonyms = []
hypernyms = []
print(original_word)
syns=wordnet.synsets(original_word)
print(syns)
for syn in syns:

	for h in syn.hypernyms(): 
		h=(h.name().split('.')[0].lower())
		hypernyms.append(h)
	for l in syn.lemmas():
		# print(l)
		synonyms.append(l.name().lower())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name().lower())
  
print(sorted(set(synonyms)))
print(sorted(set(antonyms)))
print(sorted(set(hypernyms)))

hypernyms.append(original_word)
shortest_word=original_word
for i in sorted(set(synonyms)):
	if(len(i)<len(shortest_word)): shortest_word=i 

print("SHORTEST:",shortest_word)


