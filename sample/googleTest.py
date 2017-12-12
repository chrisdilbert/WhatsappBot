from google import search
import urllib.request
from bs4 import BeautifulSoup




def google_scrape(url):
	with urllib.request.urlopen(url) as thepage:
		soup = BeautifulSoup(thepage, "html.parser")
		return soup.title.text

def google_search(query='Virat Kohali'):
   print('Hi'+query)
   i = 1
   urllist=''
   for url in search(query, stop=5):
   	    try:
   	    	a =google_scrape(url)
   	    	urllist=urllist+'\n'+a+'\n'+url+'\n'
   	    except:
   	    	  print("Exceptn ")
   	    i += 1
   	    if i==4:
   	    	break
   return urllist
