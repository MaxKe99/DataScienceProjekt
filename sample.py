import requests
from bs4 import BeautifulSoup

import logging

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor
                
questions = ['who', 'what', 'when', 'where', 'why', 'how']

def getTextAndDateFromSiteNYT(url):

    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'lxml')
    
    textAndDate = []

    textAndDate.append(soup.find('h1').text) # Headline
    try:
        textAndDate.append(soup.find('p', {"id" : "article-summary"}).text)  # Erster Paragraph
    except:
        textAndDate.append(soup.find('p', {"class" : "css-axufdj evys1bk0"}).text)  # Erster Paragraph

    text = """ """ 
    blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head', 
                'input',
                'script'
                ]
    text_raw = soup.find_all('p', {"class" : "css-axufdj evys1bk0"})
    for t in text_raw:
        if t.parent.name not in blacklist:
            text += '{} '.format(t.text)

    textAndDate.append(text) # Haupttext
    textAndDate.append(soup.time.attrs['datetime'].replace('T', ' ').replace('Z', '')[:-4]) # Datum

    return textAndDate
	
def main():
    
    log = logging.getLogger('GiveMe5W')
    log.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    log.addHandler(sh)
    
    extractor = MasterExtractor()

    url = "https://www.nytimes.com/2021/02/27/health/covid-vaccine-johnson-and-johnson.html"
    
    article = getTextAndDateFromSiteNYT(url)
    doc = Document.from_text(article[0] + " " + article[1] + " " + article[2], article[3])
    doc = extractor.parse(doc)
        
    answers = []
        
    for q in questions:
        try:
            answers.append(doc.get_top_answer(q).get_parts_as_text())
        except:
            answers.append("No answer provided.")
        
    print(url)
    for i in range(len(answers)):
        print(answers[i])
    print("\n")
        
if __name__ == '__main__':
    main()  	
	
