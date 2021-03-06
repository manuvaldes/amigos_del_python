import collections

from urllib.parse import urldefrag, urljoin, urlparse

import bs4
import requests

from pyramide.handlers import PageHandler
class Pyramide():

    # TODO usa pycharm para añadir documentación del método
    def __init__(self,startpage, singledomain=True):

        self.startpage = startpage
        self.singledomain = singledomain

    def run(self, handler: PageHandler, maxpages):
        """

        :param handler:
        :param maxpages:
        :return:
        """
        #TODO: simplemente fijate en DEQUE, un nuevo tipo del módulo collections
        pagequeue = collections.deque()  # queue of pages to be crawled
        pagequeue.append(self.startpage)
        domain = urlparse(self.startpage).netloc if self.singledomain else None
        pages = 0  # number of pages succesfully crawled so far
        failed = 0  # number of links that couldn't be crawled
        sess = requests.session()  # initialize the session
        result_dict = collections.OrderedDict()

        while pages < maxpages and pagequeue:
            url = pagequeue.popleft()  # get next page to crawl (FIFO queue)

            # read the page
            try:
                response = sess.get(url)
            except (requests.exceptions.MissingSchema,
                    requests.exceptions.InvalidSchema):
                print("*FAILED*:", url)
                failed += 1
                continue
            if not response.headers['content-type'].startswith('text/html'):
                continue  # don't crawl non-HTML content

            # Note that we create the Beautiful Soup object here (once) and
            # pass it to the other functions that need to use it
            soup = bs4.BeautifulSoup(response.text, "html.parser")

            pages += 1

            print(
                'Crawling:' + url + ' ({0} bytes)'.format(len(response.text)))

            result_dict[url] = handler.handle(soup)
            # get the links from this page and add them to the queue
            links = self._getlinks(url, domain, soup)
            for link in links:
                if not Pyramide.url_in_collection(link, result_dict.keys()) \
                        and not Pyramide.url_in_collection(link, pagequeue):
                    pagequeue.append(link)
        print('{0} pages crawled, {1} links failed.'.format(pages, failed))

        return result_dict

    # TODO revisa el warning de pycharm "method may be static"
    def _getlinks(self, pageurl, domain, soup):
        """Returns a list of links from from this page to be crawled.

        pageurl = URL of this page
        domain = domain being crawled (None to return links to *any* domain)
        soup = BeautifulSoup object for this page
        """

        # get target URLs for all links on the page
        links = [a.attrs.get('href') for a in soup.select('a[href]')]

        # remove fragment identifiers
        links = [urldefrag(link)[0] for link in links]

        # remove any empty strings
        links = [link for link in links if link]

        # if it's a relative link, change to absolute
        links = [
            link if bool(urlparse(link).netloc) else urljoin(pageurl, link) \
            for link in links]

        # if only crawing a single domain, remove links to other domains
        if domain:
            links = [link for link in links
                     if Pyramide.samedomain(urlparse(link).netloc, domain)]

        return links

    @staticmethod
    def samedomain(netloc1, netloc2):
        """Determine whether two netloc values are the same domain.

        This function does a "subdomain-insensitive" comparison. In other words

        samedomain('www.microsoft.com', 'microsoft.com') == True
        samedomain('google.com', 'www.google.com') == True
        samedomain('api.github.com', 'www.github.com') == True
        """
        domain1 = netloc1.lower()
        if '.' in domain1:
            domain1 = domain1.split('.')[-2] + '.' + domain1.split('.')[-1]

        domain2 = netloc2.lower()
        if '.' in domain2:
            domain2 = domain2.split('.')[-2] + '.' + domain2.split('.')[-1]

        return domain1 == domain2

    @staticmethod
    def url_in_collection(url, collection_obj):
        """Determine whether a URL is in a list of URLs.

        This function checks whether the URL is contained in the list with
        an http:// or https:// prefix. It is used to avoid crawling the same
        page separately as http and https.
        """
        http_version = url.replace('https://', 'http://')
        https_version = url.replace('http://', 'https://')
        return (http_version in collection_obj) or (https_version in collection_obj)
