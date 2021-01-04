from newsplease import NewsPlease

from Giveme5W1H.extractor.document import Document
from Giveme5W1H.extractor.extractor import MasterExtractor

extractor = MasterExtractor()


def main():
    article = NewsPlease.from_url(
        'https://www.foxnews.com/politics/house-democrat-subpoenas-mnuchin-irs-for-trumps-tax-returns')
    doc = Document.from_newsplease(article)
    doc = extractor.parse(doc)
    answers = []
    questions = ['who', 'what', 'when', 'where', 'why', 'how']
    for q in questions:
        doc.get_top_answer(q).get_parts_as_text()
    for i in range(len(answers)):
        print(answers[i])


if __name__ == '__main__':
    main()