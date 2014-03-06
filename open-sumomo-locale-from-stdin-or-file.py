#!/usr/local/bin/python
# coding: utf-8
import webbrowser
import sys
import os
sumomo_locale  = os.environ.get('SUMOMO_LOCALE')
print >> sys.stderr, "SUMOMO_LOCALE:", sumomo_locale
for line in sys.stdin:
  print >> sys.stderr, "slug", line
  line = line.lower().split()
  slug = line[0] 
  webbrowser.open_new_tab("https://support.mozillamessaging.com/" +\
   sumomo_locale + "/kb/" + slug)
