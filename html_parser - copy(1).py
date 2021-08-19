***
Read the documentation of the BeautifulSoup 4
 and find other ways to iterate through tags and get 
 to the juicy information
                            ***

from bs4 import BeautifulSoup

import urllib

html = urllib.urlopen('https//www.abujaelectricity.com')

html

html.code

bt = BeautifulSoup(html.read(), "lxml")

bt

bt.title

bt.title.string

bt.title.name

bt.meta

bt.meta.next

# get meta tag from html page

allMetaTags = bt.find_all('meta')

allMetaTags

allMetaTags[0]

allMetaTags[1]

allMetaTags[0]['content']

allMetaTags[0]['http-equiv']

# parsing html links

allLinks = bt.find_all('a')

len(allLinks)

allLinks[0]

allLinks[1]

allLinks[1].string

allLinks[1]['href']


## Print out all html links in a webpage

for link in allLinks: 
    print link['href']
	
## Print out all achor tags in webpage

Exercise

## print out the text in the html page

bt.get_text()

