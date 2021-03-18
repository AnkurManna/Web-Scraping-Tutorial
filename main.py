#install all requirements
#pip install requests,html5lib,bs4

import requests
from bs4 import BeautifulSoup
url = 'https://webscraper.io/test-sites/e-commerce/allinone'

# Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
# Parse the HTML

soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)
# HTML Tree Traversal

title = soup.title
print(title)

#Commonly used types of Objects
# 1. Tag
""" print(type(title))
# 2. NavigableString
print(type(title.string))
# 3. BeautifulSoup 
print(type(soup)) """
# 4. Comment 
markup = "<p><!--This is a comment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.string))
#Ftech all paragraphs
paras = soup.find_all('p')
#print(paras)

# Fetch frist para
# print(soup.find('p'))
# Fetch all span element with class glyphicon
#print(soup.find_all('span',class_="glyphicon"))

# Get text from tags
# print(soup.find('p').get_text())

#Generating Link
""" anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if link != '#' :
        all_links.add(link.get('href')) 
print(all_links)

"""

# to select a elemet with class X
# soup.select('.X')

# to select a elemet with id X
# soup.select('#X')

navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0] 
print(elem)

