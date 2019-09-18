
from pyramide import WordCountHandler,Pyramide


if __name__ == '__main__':

    handler = WordCountHandler()
    crawler = Pyramide(startpage="http://www.elpais.es" )

    result_data = crawler.run(handler,maxpages=5)

    for key,value in result_data.items():
        print(f"{key}: {value}")