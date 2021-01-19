from newsplease import NewsPlease

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor

extractor = MasterExtractor()
articles = ["https://edition.cnn.com/2021/01/11/tech/parler-amazon-lawsuit/index.html",
            "https://edition.cnn.com/2021/01/05/tech/windows-10-redesign-trnd/index.html"]
            
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
        for i in range(len(answers):
            print(answers[i])
        print("\n")
        
if __name__ == '__main__':
    main()  