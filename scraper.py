import requests 
from bs4 import BeautifulSoup
from textblob import TextBlob

def getURLFromUser():
	#Example url: http://www.ioffer.com/ratings/bags789/new-handbags-bags-shoulder-bag-627601317
	url = raw_input("Please enter the review url for seller of a product you need: ")
	print "you entered the following url: ", url
	return url

#page_url = ioffer.com url
def getCommentAndSentiment(page_url):

	#Going to scrape 3 latest pages of reviews 

	for i in range (1, 7): 
		if i == 1: 
			url = page_url 
		else:
			#http://www.ioffer.com/ratings/bags789/new-handbags-bags-shoulder-bag-627601317?page=2&sort=default
			url = page_url + "?page=" + str(i) + "&sort=default" 
			print "modified page url is :", url	
	req = requests.get(url)

	soup = BeautifulSoup(req.content, "html.parser")
	
	reviewComments = soup.find_all("a", class_="comment")


	for r in reviewComments: 
		blob = TextBlob(r.text)
		print "pageNum: ", i, " ", r.text , "==> polarity:" , str(blob.sentiment.polarity), " ; " \
		"subjectivity:", str(blob.sentiment.subjectivity)
		#using TextBlob library to do Sentiment Analysis
		
		#print(blob.sentiment.polarity)
		
	#return soup


def main():
	page_url = getURLFromUser()
	getCommentAndSentiment(page_url);

if __name__ == "__main__":
  main()
