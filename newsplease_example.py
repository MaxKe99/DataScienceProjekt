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
            'https://www.bbc.com/news/entertainment-arts-55336353']
            
questions = ['who', 'what', 'when']

def main():

    for url in articles:
        article = NewsPlease.from_url(url)
        doc = Document.from_newsplease(article)
        doc = extractor.parse(doc)
        answers = []
        print(url)
        for q in questions:
            answers.append(doc.get_top_answer(q).get_parts_as_text())
        for i in range(len(answers)):
            print(answers[i])
        print('\n')


if __name__ == '__main__':
    main()  