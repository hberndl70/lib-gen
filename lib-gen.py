# -----------------------------------------------------------------------------
# m2x 
# markdown to xml converter for the edx library generator (lib-gen)
# -----------------------------------------------------------------------------
from modules import _iof
from modules import _par 
from modules import _con 

# -----------------------------------------------------------------------------
# folder structure for output and library  
# -----------------------------------------------------------------------------
WORKING_DIR = _iof.Working_DIR()

OUTPUT = WORKING_DIR + '/' + _con.OUT_FOLDER
_iof.Delete_DIR(OUTPUT)
_iof.Create_DIR(OUTPUT)

LIBRARY_FOLDER = WORKING_DIR + '/' + _con.LIB_FOLDER 
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
MARKDOWN_FILE = WORKING_DIR + '/' + _con.INP_FOLDER + '/' + _con.INP_MD
HTML_FILE     = WORKING_DIR + '/' + _con.OUT_FOLDER + '/' + _con.OUT_HTM
XML_FILE      = WORKING_DIR + '/' + _con.OUT_FOLDER + '/' + _con.OUT_XML

TAR_FOLDER    =  _con.LIB_FOLDER + '/'
TAR_FILE      = 'library.tar'

print('converting markdown ...')
# -----------------------------------------------------------------------------
# read *.md input file (markdown_file), convert it to HTML 
# and write it into a *.html file (html_file) to disk
# -----------------------------------------------------------------------------
_iof.Write_HTML(_par.Conv_Markdown(MARKDOWN_FILE), HTML_FILE)

print('parsing html ...')
# -----------------------------------------------------------------------------
# read *.html input file (html_file), parse the HTML text
# and split it in to the information components needed to
# cerate problem structure and library.xml structure
# -----------------------------------------------------------------------------
_par.Parse_HTML(_iof.Read_HTML(HTML_FILE), XML_FILE, PROBLEM_FOLDER)

print('creating tar.gz ...')
# -----------------------------------------------------------------------------
# creating tar.gz archive of the created library folder structure
# -----------------------------------------------------------------------------
_iof.Create_TAR(WORKING_DIR, TAR_FOLDER, TAR_FILE)
