#!/usr/local/bin/python
# coding: utf-8
from bs4 import BeautifulSoup
import urllib2
import time
import sys
from datetime import datetime
import dateutil.parser
response = urllib2.urlopen(sys.argv[1])
html_search_page = response.read()
soup = BeautifulSoup(html_search_page)
all_h3 = soup.find_all('h3')
for child in soup.find_all('h3'):
    for l in child.children:
          rel_link = l.get('href')
          title = l.contents
          url = "https://support.mozilla.org/en-US" + rel_link
          response = urllib2.urlopen(url)
          html = response.read()
          s2 = BeautifulSoup(html)
          main_content  = s2.findAll("div", { "class" : "main-content" })
          first_p  = main_content[0].p.contents[0].rstrip()
          first_75 = first_p[:75] + (first_p[75:] and '..')
          time_str = s2.find_all('time')[0]['datetime']
          t2 = dateutil.parser.parse(time_str)
          date = t2.strftime("%a %B %d %Y %I:%m %p")
          #print "URL:", url
          #print "title:", title[0]
          #print "first 75:", first_75
          print "1. %s [%s](%s)--%s" % (date, title[0], url, first_75)

