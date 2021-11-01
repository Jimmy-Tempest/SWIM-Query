import re
import wikipedia
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

def queryText(text):
    queryResult = list(search(text, tld="co.in", num=10, stop=10, pause=2))
    queryResult = [result for result in queryResult if ".jpg" not in result and ".png" not in result and ".gif" not in result]
    page = requests.get(queryResult[0]).text
    soup = BeautifulSoup(page)
    # print(queryResult)
    if "wikipedia.org" in queryResult[0]:
        title = soup.select_one(".firstHeading").get_text()
        # print(title)
        searchResult = wikipedia.search(title)
        # print(searchResult)
        result = wikipedia.summary(searchResult[0]).replace("\n", " ")
    else:
        headline = soup.find('h1').get_text()
        p_tags = soup.find_all('p')
        p_tags_text = [tag.get_text().strip() for tag in p_tags]
        sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
        sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
        # Combine list items into string.
        article = ' '.join(sentence_list)
        result = summarize(article, ratio=0.3)
    return result