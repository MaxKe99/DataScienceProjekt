import logging
import os

from Giveme5W1H.extractor.extractor import MasterExtractor
from Giveme5W1H.extractor.tools.file.handler import Handler

# don`t forget to start up core_nlp_host
# giveme5w1h-corenlp

if __name__ == '__main__':
    basePath = os.path.dirname(__file__)

    # logger setup
    log = logging.getLogger('GiveMe5W')
    log.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    log.addHandler(sh)

    # giveme5w setup - with defaults
    extractor = MasterExtractor()

    inputPath = basePath + '/data/bbc.com/data'
    outputPath = basePath + '/output'
    preprocessedPath = basePath + '/cache'

    # initiate the news-please file handler with the input directory
    (Handler(inputPath)
        # add an extractor
        .set_extractor(extractor)

        # add an output directory
        .set_output_path(outputPath)

        # Optional: set a path to cache and load preprocessed documents (CoreNLP & Enhancer result)
        .set_preprocessed_path(preprocessedPath)

        # limit the documents read from the input directory (handy for development)
        # .set_limit()

        # execute it
        .process())
