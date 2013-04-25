#!/usr/bin/env python

from urllib2 import urlopen
from xml.sax import make_parser, ContentHandler
import sys

class RSSNewsFeedTagHandler(ContentHandler):

    def __init__(self):
        ContentHandler.__init__(self)
        self.__indentLevel=0

    def startElement(self,tag,attributes):
        for i in xrange(self.__indentLevel):
            sys.stdout.write("  ")
        sys.stdout.write("<%s>\n" % tag)
        self.__indentLevel += 1

    def endElement(self,tag):
        self.__indentLevel -= 1
        for i in xrange(self.__indentLevel):
            sys.stdout.write("  ")
        sys.stdout.write("<%s>\n" % tag)

class RSSNewsFeedTitleHandler(ContentHandler):
    """when planted within a stream-based parser, manage to print every single title within a RSS news feed to standard out"""
    def __init__(self):
        super(RSSNewsFeedTitleHandler, self).__init__()
        self.__inItem = False
        self.__inTitle = False

    def startElement(self,tag,attributes):
        if tag == "item":
            self.__inItem = True
        if self.__inItem and tag == "title":
            self.__inTitle = True

    def endElement(self,tag):
        if tag == "item":
            self.__inItem = False
        if tag == "title":
            sys.stdout.write("\n")
            self.__inTitle = False

    def characters(self,data):
        if self.__inTitle:
            sys.stdout.write(data)

def pullTitles(url):
    infile = urlopen(url)
    parser = make_parser()
    #parser.setContentHandler(RSSNewsFeedTagHandler)
    parser.setContentHandler(RSSNewsFeedTitleHandler)
    parser.parse(infile)


pullTitles("http://feeds.gawker.com/valleywag/full")








