
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"

def getSentences(count):
    if(count<=10):
       return count, count
    elif(count>=500):
        return count, count/20
    else:   
        return count, count/9


def summarise_doc(fileName, ACTUAL_COUNT, SENTENCES_COUNT):
    # get right number of sentences to be present in the summaried video
    SENTENCES_COUNT=int(SENTENCES_COUNT)

    print("Actual Lines: " + str(ACTUAL_COUNT) + "\t Summarised Lines: " + str(SENTENCES_COUNT))

    parser=PlaintextParser.from_file(fileName, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    file=open("summarised.txt", "w")
    chosen_sentences=[]
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        chosen_sentences.append(str(sentence)+"")
        file.write(str(sentence)+"\n")

    file.close()
    return chosen_sentences

if __name__ == "__main__":
    # url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    summarise_doc("transcript.txt", 4000, 50)