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
	#append the page and sorting query parameters to url
	url = page_url #+ "?page=100000000000000000&sort=default"

	#keep looping the page urls
	req = requests.get(url)
	print "got the req"
	soup = BeautifulSoup(req.content, "html.parser")
	print "got the soup obj"
	#print(soup.prettify())

	#review comments are under a tag, with class='comment'
	reviewComments = soup.find_all("a", class_="comment")


	for r in reviewComments: 
		blob = TextBlob(r.text)
		print r.text , "==> polarity:" , str(blob.sentiment.polarity), " ; " \
		"subjectivity:", str(blob.sentiment.subjectivity)
		#using TextBlob library to do Sentiment Analysis
		
		#print(blob.sentiment.polarity)
		
	return soup


def main():
	page_url = getURLFromUser()
	getCommentAndSentiment(page_url);

if __name__ == "__main__":
  main()
