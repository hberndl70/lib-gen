#---------------------------------------------------------------
# CLI interface for lib-gen converter
#---------------------------------------------------------------
# handling cli, checking and setting files, folders and trigger 
# conversion modules from *.md to *.xml 
#---------------------------------------------------------------
import json
import pathlib
import argparse
from modules import _con 
from modules import _iof 
from modules import _par 

def CLI():
    parser = argparse.ArgumentParser()
    parser.add_argument("library", type=str, help="name of the library")
    args = parser.parse_args()

    LIB_NAME = args.library
    if LIB_NAME == None:
        print('... library name missing!') 
        exit

    WORKING_DIR = _iof.Working_DIR()

    ASSETS = WORKING_DIR + '/' + _con.INP_FOLDER + '/' + 'assets.json'
    assets_file = pathlib.Path(ASSETS)
    if not assets_file.exists():
        print("The input file: " + ASSETS + " doesn't exist")

    CONFIG = WORKING_DIR + '/' + _con.INP_FOLDER + '/' + 'config.json'
    config_file = pathlib.Path(CONFIG)
    if not config_file.exists():
        print("The input file: " + CONFIG + " doesn't exist")
    else:
        json_data = _iof.Read_JSON(CONFIG)

    INP_MARKDOWN      =  json_data["INP_MARKDOWN"]
    OUT_HTML          =  json_data["OUT_HTML"]
    OUT_XML           =  json_data["OUT_XML"]

    # -----------------------------------------------------------------------------
    # creating folder structure for output and library  
    # -----------------------------------------------------------------------------
    OUTPUT = WORKING_DIR + '/' + _con.OUT_FOLDER
    _iof.Delete_DIR(OUTPUT)
    _iof.Create_DIR(OUTPUT)

    LIBRARY_FOLDER = WORKING_DIR + '/' + _con.LIB_FOLDER 
    _iof.Delete_DIR(LIBRARY_FOLDER)
    _iof.Create_DIR(LIBRARY_FOLDER)

    PROBLEM_FOLDER = LIBRARY_FOLDER + '/' + _con.PRB_FOLDER
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
    MARKDOWN_FILE = WORKING_DIR + '/' + _con.INP_FOLDER + '/' + INP_MARKDOWN
    HTML_FILE     = WORKING_DIR + '/' + _con.OUT_FOLDER + '/' + OUT_HTML
    XML_FILE      = WORKING_DIR + '/' + _con.OUT_FOLDER + '/' + OUT_XML
    # -----------------------------------------------------------------------------
    TAR_FOLDER    = _con.LIB_FOLDER + '/'
    TAR_FILE      = 'library-' + LIB_NAME + '.tar'
    GZ_FILE       = WORKING_DIR + '/' + TAR_FILE + '.gz'

    gz_file = pathlib.Path(GZ_FILE)
    if gz_file.exists():
        _iof.Delete_GZ(GZ_FILE)

    print('\ntesting markdown ...')
    # -----------------------------------------------------------------------------
    # read *.md input file (markdown_file), and test the structure using
    # regular expressions and re-format the text to a consisten input
    # -----------------------------------------------------------------------------
    correct = _par.Check_Markdown(MARKDOWN_FILE)

    if correct:
        print('\nconverting markdown ...')
        # -----------------------------------------------------------------------------
        # read *.md input file (markdown_file), convert it to HTML 
        # and write it into a *.html file (html_file) to disk
        # -----------------------------------------------------------------------------
        _iof.Write_HTML(_par.Conv_Markdown(MARKDOWN_FILE), HTML_FILE)
        print('... done!')
        print('\nparsing html ...')
        # -----------------------------------------------------------------------------
        # read *.html input file (html_file), parse the HTML text
        # and split it in to the information components needed to
        # cerate problem structure and library.xml structure
        # -----------------------------------------------------------------------------
        _par.Parse_HTML(_iof.Read_HTML(HTML_FILE), XML_FILE, PROBLEM_FOLDER)
        print('... done!')
        print('\ncreating tar.gz ...')
        # -----------------------------------------------------------------------------
        # creating tar.gz archive of the created library folder structure
        # -----------------------------------------------------------------------------
        _iof.Create_TAR(WORKING_DIR, TAR_FOLDER, TAR_FILE)
        print('... done!')
    else:
        print('\n')
        print('----------------------------------------')
        print('ERROR: markdown file structure incorrect')
        print('----------------------------------------')
        print('\n')