#!/usr/local/bin/python
# coding: utf-8
import webbrowser
import sys
for line in sys.stdin:
  print >> sys.stderr, "slug", line
  line = line.lower().split()
  slug = line[0] 
  webbrowser.open_new_tab("https://support.mozillamessaging.com/en-US/kb/"+slug)
