import requests 
from bs4 import BeautifulSoup
from textblob import TextBlob

def getURLFromUser():
	#Example url: http://www.ioffer.com/ratings/bags789/new-handbags-bags-shoulder-bag-627601317
	url = raw_input("Please enter the review url for seller of a product you need: ")
	print "you entered: ", url
	return url

def getNumPagesToScrape(page_url):

	#use a longNum value to determine max number of pages containing reviews
	longNum = 1000000000000
	url = page_url + "?page=" + str(longNum) + "&sort=default"
	print "modified page url to get page_nums is :", url

	req = requests.get(url)
	soup = BeautifulSoup(req.content, "html.parser")
	pagination = soup.find("div", class_="pagination")
	anchors = pagination.find_all("a")

	#the last anchor contains the num_pages
	num_pages = anchors[len(anchors)-1].text
	print(num_pages)

	#conver Unicode to int before returning
	return int(num_pages)
	
def getCommentAndSentiment(page_url, num_pages):

	#Scrapes reviews on all available pages 
	for i in range (1, num_pages + 1): 
		url = page_url + "?page=" + str(i) + "&sort=default" 
		
	
	req = requests.get(url)
	soup = BeautifulSoup(req.content, "html.parser")
	reviewComments = soup.find_all("a", class_="comment")

	for revComment in reviewComments: 
		blob = TextBlob(revComment.text)
		print "pageNum: ", i, " ", revComment.text , \
		"==> polarity:" , str(blob.sentiment.polarity), " ; " \
		"subjectivity:", str(blob.sentiment.subjectivity)

def main():
	page_url = getURLFromUser()
	num_pages = getNumPagesToScrape(page_url)
	getCommentAndSentiment(page_url, num_pages);

if __name__ == "__main__":
  main()
