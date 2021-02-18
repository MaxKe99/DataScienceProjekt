import requests
from bs4 import BeautifulSoup

import logging

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor

articles = ["https://www.bbc.com/news/uk-scotland-scotland-politics-55396311"]
            
questions = ['who', 'what', 'when', 'where', 'why', 'how']

def getTextAndDateFromSite(url):
	res = requests.get(url)
	html_page = res.content
	
	soup = BeautifulSoup(html_page, 'lxml')
	text = soup.find_all('p')
	
	result = []
	
	result.append(soup.find('h1').text)
	result.append(soup.find('p').text)
	
	output = """ """
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

	for t in text:
		if t.parent.name not in blacklist:
			output += '{} '.format(t.text)
			
			
	result.append(output)
	result.append(soup.time.attrs['datetime'].replace('T', ' ').replace('Z', '')[:-4])
		
	return result
	
def main():
    
    log = logging.getLogger('GiveMe5W')
    log.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    log.addHandler(sh)
    
    extractor = MasterExtractor()
    
    for url in articles:
        article = getTextAndDateFromSite(url)
        doc = Document.from_text(article[0] + article[1] +article[2], article[3])
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
	