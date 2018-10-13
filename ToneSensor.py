import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

sia = SIA()

def article_polarity(article):
	pol_score = sia.polarity_scores(article)
	return pol_score

def return_keywords(headline)	
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(headline.lower()) 
	filtered_sentence = [w for w in word_tokens if not w in stop_words] 
	filtered_sentence = []
	for w in word_tokens: 
		if w not in stop_words: 
			filtered_sentence.append(w)
	return filtered_sentence