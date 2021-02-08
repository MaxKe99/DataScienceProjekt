import requests
from bs4 import BeautifulSoup

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor

extractor = MasterExtractor()
articles = ["https://www.nytimes.com/2020/12/11/arts/dance/othella-dallas-dead.html"]
            
questions = ['who', 'what', 'when', 'where', 'why', 'how']

def getTextAndDateFromSite(url):
	res = requests.get(url)
	html_page = res.content
	
	soup = BeautifulSoup(html_page, 'lxml')
	text = soup.find_all('p')
	
	result = ["", ""]
	
	output = output = soup.find('h1').text + ' '
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
			
			
	result[0] = output
		
	time = soup.find('time')
	if time.has_attr('datetime'):
		result[1] = time['datetime']
		
	return result
	
def main():

    for url in articles:
        article = getTextAndDateFromSite(url)
        doc = Document.from_text(article[0], article[1])
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
	