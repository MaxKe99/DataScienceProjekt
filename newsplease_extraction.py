from newsplease import NewsPlease

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor

extractor = MasterExtractor()
articles = ['https://www.bbc.com/news/business-55390858',
            'https://www.bbc.com/news/business-55384111',
            'https://www.bbc.com/news/business-55359320',
            'https://www.bbc.com/news/business-55344670',
            'https://www.bbc.com/news/business-55357340',
            'https://www.bbc.com/news/entertainment-arts-55393972',
            'https://www.bbc.com/news/entertainment-arts-55392779',
            'https://www.bbc.com/news/entertainment-arts-55358301',
            'https://www.bbc.com/news/entertainment-arts-55346397',
            'https://www.bbc.com/news/entertainment-arts-55336353',
            'https://www.bbc.com/news/uk-politics-55422729',
            'https://www.bbc.com/news/uk-politics-55410349',
            'https://www.bbc.com/news/uk-politics-55414981',
            'https://www.bbc.com/news/uk-scotland-scotland-politics-55396311',
            'https://www.bbc.com/news/uk-wales-politics-55423293',
            'https://www.bbc.com/sport/football/55382530',
            'https://www.bbc.com/sport/tennis/55416994',
            'https://www.bbc.com/sport/golf/55395828',
            'https://www.bbc.com/sport/athletics/55257397',
            'https://www.bbc.com/sport/cycling/55337877',
            'https://www.bbc.com/news/technology-55438969',
            'https://www.bbc.com/news/technology-55439190',
            'https://www.bbc.com/news/technology-55403473',
            'https://www.bbc.com/news/technology-55415350',
            'https://www.bbc.com/news/technology-55426212',
            "https://edition.cnn.com/2020/12/18/investing/tesla-sp500-winners/index.html",
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
            "https://www.nytimes.com/2020/12/21/business/eurostar-pandemic-train-europe.html",
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
            "https://www.euronews.com/2020/10/02/cutting-carbon-emissions-and-power-costs-in-southeast-asia"]
            
questions = ['who', 'what', 'when', 'where', 'why', 'how']

def main():

    for url in articles:
        article = NewsPlease.from_url(url)
        doc = Document.from_newsplease(article)
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