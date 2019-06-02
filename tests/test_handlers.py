#!/usr/bin/env python
from pyramide import handlers
import pytest


#TODO haz un fixture de HTML parseado a partir de este string
HTML_STRING="""
<!DOCTYPE html>
<html>
<body>
<h1>Esta es la cabecera del documento</h1>
<p>Esto es un párrafo del documento. Está formado por dos frases.</p>
</body>
</html>"""
@pytest.fixture
def html_soup():
    pass


#TODO haz un test para la funcion noalpha
def test_noalpha():
    pass

#TODO haz un test para la funcion getwords
def test_getwords():
    pass


#TODO haz un test de WordCountHandler usando el fixture html_soup
def test_wordcounthandler(html_soup):
    pass
