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
#print(soup.prettify())
#for link in soup.find_all('a'):
#    print(link.get('href'))
all_h3 = soup.find_all('h3')
#for link in all_h3.find_all('a'):
#    print(link.get('href'))
#print "all_h3[0]:", all_h3[0]
#print "title:", all_h3[0].title
for child in soup.find_all('h3'):
    for l in child.children:
          rel_link = l.get('href')
          #print "rel_relink", rel_link
          title = l.contents
          url = "https://support.mozilla.org/en-US" + rel_link
          #print "url:", url
          response = urllib2.urlopen(url)
          html = response.read()
          s2 = BeautifulSoup(html)
          main_content  = s2.findAll("div", { "class" : "main-content" })
          first_p  = main_content[0].p.contents[0].rstrip()
          first_75 = first_p[:75] + (first_p[75:] and '..')
          #print first_75
          #asked_on = s2.findAll("div", {"class" : "asked-on" })
          time_str = s2.find_all('time')[0]['datetime']
          t2 = dateutil.parser.parse(time_str)
          #time_str = asked_on[0].time.contents
          #t2 = time.strptime(time_str[0], '%m/%d/%y %I:%M %p')
          #print time.asctime(t2)
          print "date:", t2.strftime("%a %B %d %Y %I:%m %p")
          print "URL:", url
          print "title:", title[0]
          print "first 75:", first_75

