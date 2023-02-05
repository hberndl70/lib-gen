# -----------------------------------------------------------------------------
# lib-gen
# markdown to xml converter for chechbox problems stored in an edx library 
# -----------------------------------------------------------------------------
import time
from modules import _iof
from modules import _par 
from modules import _con 

# -----------------------------------------------------------------------------
# START Time
# -----------------------------------------------------------------------------
start = time.time()

# -----------------------------------------------------------------------------
# folder structure for output and library  
# -----------------------------------------------------------------------------
OUTPUT = _iof.Working_DIR() + '/' + _con.OUT_FOLDER
_iof.Delete_DIR(OUTPUT)
_iof.Create_DIR(OUTPUT)

LIBRARY_FOLDER = _iof.Working_DIR() + '/' + _con.LIB_FOLDER 
_iof.Delete_DIR(LIBRARY_FOLDER)
_iof.Create_DIR(LIBRARY_FOLDER)

PROBLEM_FOLDER = LIBRARY_FOLDER + '/' + _con.PRO_FOLDER
_iof.Create_DIR(PROBLEM_FOLDER)

POLICIES_FOLDER = LIBRARY_FOLDER + '/' + _con.POL_FOLDER
_iof.Create_DIR(POLICIES_FOLDER)

# -----------------------------------------------------------------------------
# copy policy file (assets.json) into policies folder 
# -----------------------------------------------------------------------------
policy_file = _con.INP_FOLDER + '/' + _con.POL_FILENAME
_iof.Copy_POL(policy_file, POLICIES_FOLDER)

# -----------------------------------------------------------------------------
# conversion file - input / ouput - setup 
# -----------------------------------------------------------------------------
markdown_file = _iof.Working_DIR() + '/' + _con.INP_FOLDER + '/' + _con.INP_MD
html_file     = _iof.Working_DIR() + '/' + _con.OUT_FOLDER + '/' + _con.OUT_HTM

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

print('\nwriting library structure ...')
# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------

print('\ncreating edx library ...')
# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# END Time
# -----------------------------------------------------------------------------
end = time.time()
print('\nexecution time in seconds:')
print(end - start)