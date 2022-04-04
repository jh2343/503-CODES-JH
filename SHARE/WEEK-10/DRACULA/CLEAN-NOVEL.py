#conda install -c anaconda nltk
#inside python run: import nltk; 
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('stopwords')

#---------------------------
#NOTES
#---------------------------

#NOTE: string.printable will give the all sets of punctuation, 
#	   digits, ascii_letters and whitespace.


import nltk
import string
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt


#USER PARAM
input_path			=	'DRACULA.txt'
chunk_size			=	0 			#if 0 use sentances if >0 use chuncks with "chunk_size" characters
compute_sentiment 	=	True		
sentiment    		=	[]			#average sentiment of each chunck of text 
ave_window_size		=	250			#size of scanning window for moving average
					

#OUTPUT FILE
output='transactions.txt'
if os.path.exists(output): os.remove(output)

#INITIALIZE
lemmatizer 	= 	WordNetLemmatizer()
ps 			=	PorterStemmer()
sia 		= 	SentimentIntensityAnalyzer()

#ADD MORE
stopwords	=	stopwords.words('english')
add=['mr','mrs','wa','dr','said','back','could','one','looked','like','know','around','dont']
for sp in add: stopwords.append(sp)

def moving_ave(y,w=100):
	#W=WINDOW SIZE (NUMBER OF NEIGHBORING POINTS TO AVERAGE)
 	#AVERAGING WINDOW (3 --> +1 0 -1)
	mask=np.ones((1,w))/w; mask=mask[0,:] 
	#Convolve the mask with the raw data
	return np.convolve(y,mask,'same')

def read_and_clean(path,START=0,STOP=-1):
	global sentiment 

	#READ IN AS ONE BIG STING
	file = open(path, 'rt')
	text = file.read().lower()	#CONVERT TO LOWER CASE
	file.close()

	#MAKE INTO NLTK OBJECT AND SEARCH TEXT 
	# nltk_object=nltk.Text(word_tokenize(text))
	# print(nltk_object.concordance("dracula")) 	#SEARCH TEXT
	# nltk_object.dispersion_plot(["dracula", "jonathan","mina"])

	#REMOVE HEADER, AND NEW LINES
	text=text.replace("'",'') #wasn't --> wasnt
	lines = text.splitlines(); text=''; 
	lines=lines[START:STOP]    # mystring.replace('\n', ' ')
	for line in lines: text=text+' '+line

	#ONLY KEEP CHAR IN PRINTABLE
	tmp=''; printable = set(string.printable); # print(printable)
	for char in text:
		if(char in printable): tmp=tmp+char
	text=tmp


	#BREAK INTO CHUNKS (SENTANCES OR OTHERWISE)
	if(chunk_size==0): sentences=nltk.tokenize.sent_tokenize(text)  #SENTENCES

	if(chunk_size>0):
		sentences=[]; size=500; i1=0; i2=size
		while(i2<len(text)):
			sentences.append(text[i1:i2])
			i1+=size; i2+=size
	print("NUMBER OF CHUNKS FOUND:",len(sentences))


	#CLEAN SENTENCES AND LEMMATIZE
	keep='0123456789abcdefghijklmnopqrstuvwxy';

	new_sentences=[]; vocabulary=[]
	for sentence in sentences:
		new_sentence=''

		for word in sentence.split():
			
			#ONLY KEEP CHAR IN "keep"
			tmp2=''
			for char in word: 
				if(char in keep): 
					tmp2=tmp2+char
				else:
					tmp2=tmp2+' '

			#STEM OF LEMMATIZE
			word=tmp2
			new_word=lemmatizer.lemmatize(word) #LEMMATIZATION

			#REMOVE WHITE SPACES
			new_word=new_word.replace(' ', '')

			#BUILD NEW SENTANCE BACK UP
			if( new_word not in stopwords):
				if(new_sentence==''):
					new_sentence=new_word
				else:
					new_sentence=new_sentence+','+new_word
				if(new_word not in vocabulary): vocabulary.append(new_word)

		if(compute_sentiment):
			text1=new_sentence.replace(',',' ')
			score=sia.polarity_scores(text1)
			sentiment.append([score['neg'],score['neu'],score['pos'],score['compound']])
		#SAVE SENTANCE TO OUTPUT FILE
		if(len(new_sentence.split(','))>2):
			f = open(output, "a")
			f.write(new_sentence+"\n")
			f.close()

	sentiment=np.array(sentiment)
	print("TOTAL AVERAGE SENTEMENT:",np.mean(sentiment,axis=0))
	print("VOCAB LENGTH",len(vocabulary))


	if(compute_sentiment):
		#TAKE SENTIMENT MOVING AVE AND RENORMALIZE
		neg=moving_ave(sentiment[:,0],ave_window_size);  neg=(neg-np.mean(neg))/np.std(neg)
		neu=moving_ave(sentiment[:,1],ave_window_size);  neu=(neu-np.mean(neu))/np.std(neu)
		pos=moving_ave(sentiment[:,2],ave_window_size);  pos=(pos-np.mean(pos))/np.std(pos)
		cmpd=moving_ave(sentiment[:,3],ave_window_size); cmpd=(cmpd-np.mean(cmpd))/np.std(cmpd)

		#PLOT SENTIMENT
		indx=np.linspace(0,len(sentiment),len(sentiment))
		plt.plot(indx,neg, label="negative")
		# plt.plot(indx,neu, label="neutral")
		plt.plot(indx,pos, label="positive")
		plt.plot(indx,cmpd, label="combined")

		plt.legend(loc="upper left")

		plt.xlabel("text chunks: progression of book")
		plt.ylabel("sentiment")
		plt.show()

#RUN FUNCTION
read_and_clean(input_path,400,-400)
#print(sentiment)
