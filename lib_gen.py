# -----------------------------------------------------------------------------
# m2x 
# markdown to xml converter for the edx library generator (lib-gen)
# -----------------------------------------------------------------------------
# import time
from modules import _iof
from modules import _par 

# -----------------------------------------------------------------------------
# START Time
# -----------------------------------------------------------------------------
# start = time.time()

# -----------------------------------------------------------------------------
# TESTING SETUP
# constant defined as string with absolute path + filename 
# -----------------------------------------------------------------------------
FILE_MD  = "/Users/hansberndl/_git/lib-gen/input/test.md"
FILE_HTM = "/Users/hansberndl/_git/lib-gen/output/test.html"
# -----------------------------------------------------------------------------
markdown_file = "" + FILE_MD
html_file     = "" + FILE_HTM

print('\nconverting markdown to html ...')
# -----------------------------------------------------------------------------
# read *.md input file (markdown_file), convert it to HTML 
# and write it into a *.html file (html_file) to disk
# -----------------------------------------------------------------------------
_iof.Write_HTML(_par.Conv_Markdown(markdown_file), html_file)

print('\nconverting html to xml ...')
# -----------------------------------------------------------------------------
# read *.html input file (html_file), parse the HTML text
# and split it in to the information components needed to
# cerate problem structure and library.xml structure
# -----------------------------------------------------------------------------
_par.Parse_HTML(_iof.Read_HTML(html_file))

# -----------------------------------------------------------------------------
# END Time
# -----------------------------------------------------------------------------
# end = time.time()
# print('\nexecution time in seconds:')
# print(end - start)