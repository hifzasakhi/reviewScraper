import requests 
from bs4 import BeautifulSoup

#Input = ioffer.com url
def getNumWebPages(page_url):
	#append the page and sorting query parameters to url
	url = page_url + "?page=100000000000000000&sort=default"
	req = requests.get(url)
	soup = BeautifulSoup(req.content)
	return soup




def retrieveImageExtension(image_url):
  file_ext = '.'+ image_url.split('.')[-1]
  print("file_ext is: " + file_ext)
  return file_ext


if __name__ == "__main__":
  app.run(port=8000)
