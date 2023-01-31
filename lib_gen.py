import os
import sys

from modules import _m2h
from modules import _iof
from modules import _par 

# -----------------------------------------------------------------------------
print('\n')
print('----------------------------------------------------------------')
print('==- =- E =-= D =-= X -=- L =-= I =-= B -=- G =-= E =-= N -= -===')
print('----------------------------------------------------------------')
print('\n')
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TESTING SETUP
# constant defined as string with absolute path + filename 
# -----------------------------------------------------------------------------
FILE_MD  = "/Users/hansberndl/_tst/md2xml/test.md"
FILE_HTM = "/Users/hansberndl/_tst/md2xml/test.html"
FILE_XML = "/Users/hansberndl/_tst/md2xml/test.xml"
# -----------------------------------------------------------------------------

markdown_file = "" + FILE_MD
html_file     = "" + FILE_HTM
xml_file      = "" + FILE_XML

print('... converting markdown to html \n')
# -----------------------------------------------------------------------------
# read *.md input file (markdown_file), convert it to HTML 
# and write it into a *.html file (html_file) to disk
# -----------------------------------------------------------------------------
_iof.write_html(_m2h.conv_md2html(markdown_file), html_file)

print ('... parsing \n')
# -----------------------------------------------------------------------------
# read *.html input file (html_file), parse the HTML text
# and split it in to the information components needed to
# cerate problem structure and library.xml structure
# -----------------------------------------------------------------------------
_par.parse_html(_iof.read_html(html_file))
