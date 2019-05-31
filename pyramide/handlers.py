import collections
import string

from abc import ABC, abstractmethod


class PageHandler(ABC):

    @abstractmethod
    def handle(self, soup):
        pass


class WordCountHandler(PageHandler):

    def handle(self, soup):
        """Function to be customized for processing of a single page.

        pageurl = URL of this page
        pageresponse = page content; response object from requests module
        soup = Beautiful Soup object created from pageresponse

        Return value = whether or not this page's links should be crawled.
        """
        self._wordcount(soup)  # display unique word counts
        return True

    def _wordcount(self,soup):
        """Display word counts for a crawled page.

        pageresponse = page content; response object from requests module
        soup = Beautiful Soup object created from pageresponse

        This is an example of a page handler. Just creates a list of unique
        words on the page and displays the word counts.
        """
        rawtext = soup.get_text()
        print(rawtext)
        words = WordCountHandler.getwords(rawtext)
        counts, _ = WordCountHandler.getcounts(words)
        if counts.most_common(1)[0][1] < 10:
            print('This page does not have any words used more than 10 times.')
        else:
            print(counts.most_common(10))

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
        shortwords = [word for word in counts if len(word) < 3]
        ignore = shortwords + \
                 ['after', 'all', 'and', 'are', 'because', 'been', 'but', 'for', 'from',
                  'has', 'have', 'her', 'more', 'not', 'now', 'our', 'than', 'that',
                  'the', 'these', 'they', 'their', 'this', 'was', 'were', 'when', 'who',
                  'will', 'with', 'year', 'hpv19slimfeature', 'div']
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
        cruft = ',./():;!"' + "<>'â{}  "  # characters to strip off ends of words
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
        #TODO puedes refactorizar este bloque usando any()

        for char in word:
            if char.isalpha():
                return False
        return True
