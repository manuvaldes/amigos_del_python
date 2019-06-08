
from pyramide import WordCountHandler,Pyramide


if __name__ == '__main__':

    handler = WordCountHandler()
    crawler = Pyramide(startpage="http://www.elpais.es" )

    crawler.run(handler,maxpages=1)