import requests
from bs4 import BeautifulSoup

import logging

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor

articles = ["https://edition.cnn.com/2020/12/18/investing/tesla-sp500-winners/index.html",
            "https://edition.cnn.com/2020/12/20/investing/elon-musk-bitcoin-dogecoin/index.html",
            "https://edition.cnn.com/2020/12/21/business/uk-ports-covid-brexit-shortages/index.html",
            "https://edition.cnn.com/2020/12/21/business/walmart-returns-at-home/index.html",
            "https://edition.cnn.com/2020/12/21/investing/dow-stock-market-today-coronavirus/index.html",
            "https://edition.cnn.com/2020/12/21/entertainment/movies-2020-column/index.html",
            "https://edition.cnn.com/2020/12/22/entertainment/chris-pratt-chris-evans-chris-hemsworth/index.html",
            "https://edition.cnn.com/2020/12/22/entertainment/rachel-zoe-son-falls-ski-lift/index.html",
            "https://edition.cnn.com/2020/12/21/entertainment/zooey-deschanel-katy-perry-music-video-trnd/index.html",
            "https://edition.cnn.com/2020/12/21/entertainment/ed-sheeran-afterglow-song/index.html",
            "https://edition.cnn.com/2020/12/22/politics/biden-key-lines-christmas-address/index.html",
            "https://edition.cnn.com/2021/01/11/politics/biden-oath-of-office-capitol/index.html",
            "https://edition.cnn.com/2020/12/22/politics/biden-twitter-white-house-accounts/index.html",
            "https://edition.cnn.com/2020/12/22/politics/alex-padilla-senate-gavin-newsom/index.html",
            "https://edition.cnn.com/2020/12/22/politics/daca-texas/index.html",
            "https://edition.cnn.com/2020/12/23/sport/los-angeles-lakers-clippers-ring-ceremony-nba-championship-spt-intl/index.html",
            "https://edition.cnn.com/2020/12/23/football/lionel-messi-break-pele-record-barcelona-valladolid-spt-intl/index.html",
            "https://edition.cnn.com/2020/12/23/sport/tokyo-olympic-games-opening-closing-ceremonies-spt-intl/index.html",
            "https://edition.cnn.com/2020/12/21/sport/tom-brady-atlanta-falcons-tampa-bay-buccaneers-new-england-patriots-nfl-spt-intl/index.html",
            "https://edition.cnn.com/2020/12/22/sport/pittsburgh-steelers-cincinnati-bengals-muppets-nfl-spt-intl/index.html",
            "https://edition.cnn.com/2021/01/11/tech/parler-amazon-lawsuit/index.html",
            "https://edition.cnn.com/2021/01/05/tech/windows-10-redesign-trnd/index.html",
            "https://edition.cnn.com/2020/12/18/tech/smic-us-sanctions-intl-hnk/index.html",
            "https://edition.cnn.com/2020/12/23/tech/nikola-garbage-truck-canceled/index.html",
            "https://edition.cnn.com/2020/12/18/tech/alibaba-cloud-ipvm-uyghurs-intl-hnk/index.html",
            ]
            
questions = ['who', 'what', 'when', 'where', 'why', 'how']

def monthHelper(str):
    if str[:7] == "January ":
        return "01-" + str[-3:-1]
    elif str[:8] == "December":
        return "12-" + str[-2:]
    else:
        return "00"

def getTextAndDateFromSite(url):
	res = requests.get(url)
	html_page = res.content
	
	soup = BeautifulSoup(html_page, 'lxml')
	text = soup.find_all("div", {"class": "zn-body__paragraph"})
	
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
	date = soup.find("p", {"class": "update-time"}).text[28:][:17]
	dateForm = ""
	dateForm += date[-4:] + "-" + monthHelper(date[:11])
	result.append(dateForm)
		
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
	