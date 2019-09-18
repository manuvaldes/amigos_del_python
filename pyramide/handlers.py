import collections
import string

from abc import ABC, abstractmethod


class PageHandler(ABC):
    #TODO Fijate! no habiamos visto el decorador @abstractmethod
    @abstractmethod
    def handle(self, soup):
        """Function to be customized for processing of a single page.

        pageurl = URL of this page
        pageresponse = page content; response object from requests module
        soup = Beautiful Soup object created from pageresponse

        Return value = data processed from URL
        """
        pass


class WordCountHandler(PageHandler):

    def __init__(self,max_words=5):

        self.max_words=max_words

    def handle(self, soup):

        """Display word counts for a crawled page.

        pageresponse = page content; response object from requests module
        soup = Beautiful Soup object created from pageresponse

        This is an example of a page handler. Just creates a list of unique
        words on the page and displays the word counts.
        """
        rawtext = soup.get_text()
        words = WordCountHandler.getwords(rawtext)
        counts, _ = WordCountHandler.getcounts(words)

        #TODO: tendrás que parametrizar el valor 5, ¿cómo puedes hacerlo manteniendo retrocompatibilidad?
        return counts.most_common(self.max_words)

    @staticmethod
    def getcounts(words=None):
        """Convert a list of words into a dictionary of word/count pairs.
        Does not include words not deemed interesting.
        """

        # create a dictionary of key=word, value=count
        counts = collections.Counter(words)

        # save total word count before removing common words
        wordsused = len(counts)

        # remove common words from the dictionary
        ignore = [word for word in counts if len(word) < 4]
        for word in ignore:
            counts.pop(word, None)

        # remove words that contain no alpha letters
        tempcopy = [_ for _ in words]
        for word in tempcopy:
            if WordCountHandler.noalpha(word):
                counts.pop(word, None)

        return (counts, wordsused)

    @staticmethod
    def getwords(rawtext):
        """Return a list of the words in a text string.
        """
        words = []
        # characters to strip off ends of words
        cruft = ',./():;!"' + "<>'â{}  "
        for raw_word in rawtext.split():
            # remove whitespace before/after the word
            word = raw_word.strip(string.whitespace + cruft + '-').lower()

            # remove posessive 's at end of word
            if word[-2:] == "'s":
                word = word[:-2]

            if word:  # if there's anything left, add it to the words list
                words.append(word)

        return words

    @staticmethod
    def noalpha(word):
        # TODO refactoriza este bloque en una sola linea usando any()
        for char in word:
            if char.isalpha():
                return False
        return True
