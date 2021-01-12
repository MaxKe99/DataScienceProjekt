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
            'https://www.bbc.com/news/technology-55426212']
            


def main():

    questions = ['who', 'what', 'when', 'where']
    for url in articles:
        article = NewsPlease.from_url(url)
        doc = Document.from_newsplease(article)
        doc = extractor.parse(doc)
        answers = []
        print(url)
        try:
            for q in questions:
                answers.append(doc.get_top_answer(q).get_parts_as_text())
        
            for i in range(len(answers)):
                print(answers[i])
        
        except:
            print("Giveme5W1H could not find the answers.")
            
        finally:
            print('\n')

if __name__ == '__main__':
    main()  