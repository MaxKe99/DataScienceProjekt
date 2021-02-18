import requests
from bs4 import BeautifulSoup

import logging

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor

articles = ["https://www.nytimes.com/2020/12/21/business/eurostar-pandemic-train-europe.html",
            "https://www.nytimes.com/2020/12/20/business/economy/stimulus-bill-congress.html",
            "https://www.nytimes.com/2020/12/21/business/stocks-sink-as-a-fast-spreading-virus-strain-emerges-in-britain-and-overshadows-a-stimulus-deal.html",
            "https://www.nytimes.com/2020/12/17/business/the-bank-of-england-holds-interest-rates-steady-as-brexit-talks-continue.html",
            "https://www.nytimes.com/2020/12/17/business/coinbase-ipo.html",
            "https://www.nytimes.com/2020/12/20/arts/television/snl-joe-biden-jim-carrey-kristen-wiig.html",
            "https://www.nytimes.com/2020/12/17/movies/kim-ki-duk-dead.html",
            "https://www.nytimes.com/2020/12/11/arts/dance/othella-dallas-dead.html",
            "https://www.nytimes.com/2020/11/24/arts/television/chappelles-show-netflix.html",
            "https://www.nytimes.com/2020/12/16/arts/music/break-it-all-latin-rock-netflix.html",
            "https://www.nytimes.com/2020/12/22/us/politics/trump-pardons.html",
            "https://www.nytimes.com/2020/12/22/us/politics/trump-coronavirus-bill.html",
            "https://www.nytimes.com/2020/12/22/us/politics/mbs-saudi-immunity-trump.html",
            "https://www.nytimes.com/2020/12/22/us/politics/whats-in-the-covid-relief-bill.html",
            "https://www.nytimes.com/2020/12/21/us/politics/coronavirus-stimulus-deal.html",
            "https://www.nytimes.com/2020/12/16/sports/soccer/liverpool-tottenham.html",
            "https://www.nytimes.com/2020/12/16/sports/soccer/concussion-substitutes-ifab.html",
            "https://www.nytimes.com/2020/12/15/sports/basketball/wme-endeavor-bda-sports-bill-duffy.html",
            "https://www.nytimes.com/2020/12/14/sports/golf/us-womens-open-winner-a-lim-kim.html",
            "https://www.nytimes.com/2020/12/14/sports/baseball/jared-porter-mets.html",
            "https://www.nytimes.com/2020/12/18/technology/big-tech-should-try-radical-candor.html",
            "https://www.nytimes.com/2020/12/18/technology/cyberpunk-2077-refund.html",
            "https://www.nytimes.com/2020/12/17/technology/google-antitrust-monopoly.html",
            "https://www.nytimes.com/2020/12/22/technology/augmented-reality-online-shopping.html",
            "https://www.nytimes.com/2020/12/22/technology/georgia-senate-runoff-misinformation.html",
            "https://www.euronews.com/2020/12/17/google-sued-by-10-us-states-for-anti-competitive-online-ad-sales",
            "https://www.euronews.com/2020/12/21/global-challenges-turned-into-constructive-solutions-for-all",
            "https://www.euronews.com/2020/11/17/europe-s-gdpr-provides-our-privacy-model-around-the-world-apple-vp-says",
            "https://www.euronews.com/2020/11/17/don-t-cut-back-on-military-spending-because-of-covid-19-european-defence-chief-warns",
            "https://www.euronews.com/2020/11/17/how-can-recycling-help-the-european-union-achieve-its-green-targets",
            "https://www.euronews.com/living/2020/07/01/zac-efron-looks-for-solutions-to-climate-change-in-new-netflix-series",
            "https://www.euronews.com/2019/11/06/catherine-deneuve-76-treated-in-paris-hospital-after-limited-stroke-afp",
            "https://www.euronews.com/2019/06/27/alanis-morissette-pregnancy-45-i-had-freak-out-joy-freak-t157206",
            "https://www.euronews.com/living/2019/08/22/stella-mccartney-and-taylor-swift-team-up-for-clothing-and-accessories",
            "https://www.euronews.com/2019/05/01/pink-reveals-she-had-miscarriage-17-you-feel-your-body-t153175",
            "https://www.euronews.com/2020/10/08/spanish-government-wants-to-repeal-parental-consent-rule-for-abortions",
            "https://www.euronews.com/2020/08/06/twitter-to-label-government-officials-and-state-backed-news-accounts",
            "https://www.euronews.com/2019/11/12/president-jimmy-carter-undergo-procedure-relieve-pressure-brain-falls-n1080361",
            "https://www.euronews.com/2019/11/09/bloomberg-faces-big-challenges-if-he-leaps-into-2020-white-house-race",
            "https://www.euronews.com/2019/11/08/former-nyc-mayor-michael-bloomberg-considering-jump-into-us-presidential-race",
            "https://www.euronews.com/2020/12/14/champions-league-draw-sees-neymar-s-psg-take-on-barcelona-as-holders-bayern-face-lazio",
            "https://www.euronews.com/2020/11/19/new-fifa-rules-to-protect-female-players-maternity-rights",
            "https://www.euronews.com/2020/12/01/premier-league-postpones-first-fixture-since-resumption-during-covid-19-pandemic",
            "https://www.euronews.com/2020/10/31/england-win-2020-six-nations-championship-after-ireland-fail-in-paris",
            "https://www.euronews.com/2020/10/29/coronavirus-russia-wants-to-keep-sports-fans-in-stadiums-despite-covid-19-pandemic",
            "https://www.euronews.com/2020/12/21/new-hacking-scams-here-s-how-to-avoid-them",
            "https://www.euronews.com/2020/12/19/humans-and-robots-battle-it-out-for-control-of-the-future",
            "https://www.euronews.com/2020/11/26/europe-signs-86-million-deal-to-bring-space-trash-home",
            "https://www.euronews.com/2020/11/09/a-win-for-global-human-rights-as-eu-agrees-on-tighter-rules-for-surveillance-tech-exports",
            "https://www.euronews.com/2020/10/02/cutting-carbon-emissions-and-power-costs-in-southeast-asia"
            ]
            
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
	