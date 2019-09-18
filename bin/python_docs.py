
from pyramide import WordCountHandler,Pyramide


if __name__ == '__main__':

    handler = WordCountHandler(10)
    crawler = Pyramide(startpage="https://docs.python.org/3/" )

    result_data = crawler.run(handler,maxpages=20)

    for key,value in result_data.items():
        print(f"{key}: {value}")