#!/usr/bin/env python

import bs4
import codecs
import sys


"""
Uses beautifulsoup4 to extract the relevant text of an HTML source document while attempting to leave elements
that make the result a readable HTML document.

Things to try:

- find nice input for each thing? store this file?
- GET ENCODINGS CORRECT!
- Deal with malformed javascript or issues that stop parsing
- Get parents of strings, so we know that we're not missing anything???

"""

TAGLIST = ['a','p','li','ul','ol','h1','h2','h3']

def getAllUsefulText():
    doc = sys.stdin.read()
    soup = bs4.BeautifulSoup(doc)
    for tag in soup.findAll(["script","style"]):    # Remove javascript strings
        tag.string = ""
    for tag in soup.findAll(True):
        tag.attrs=[]    # Remove attributes to keep things clean
        if isinstance(tag,bs4.Tag) and tag.name in TAGLIST:
            print(tag)
	

getAllUsefulText()





