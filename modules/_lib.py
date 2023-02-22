# --------------------------------------------------------------
# writing the library.xml file
# --------------------------------------------------------------
# this file is the inventory file for the edx library it holds 
# the information:  display_name="xxx" org="yyy" library="zzz" 
# and addintional paramaters as well as the list of all library 
# components stored in the corresponding folder.
# --------------------------------------------------------------
from lxml import etree
from modules import _con 
from modules import _iof

def Write_LIB_XML(cbp_number):
    WORKING_DIR = _iof.Working_DIR()
    CONFIG = WORKING_DIR + '/' + _con.INP_FOLDER + '/' + _con.CFG_FILENAME

    json_data = _iof.Read_JSON(CONFIG)
    DISPLAY_NAME = json_data["DISPLAY_NAME"]
    LIBRARY      = json_data["LIBRARY"]
    ORG          = json_data["ORG"]

    library = etree.Element('library')
    library.set ('url_name',      _con.URL_NAME)
    library.set ('xblock-family', _con.XBLOCK_FAMILY)
    library.set ('display_name',       DISPLAY_NAME)
    library.set ('org',                ORG)
    library.set ('library',            LIBRARY)

    i = 1
    while i <= cbp_number:
        CBP_FILENAME = _iof.Create_Name32(str(_con.CBP_XML), str(i))
        problem = etree.SubElement(library, 'problem')
        problem.set ("url_name", CBP_FILENAME )
        i += 1

    xml_block = etree.tostring(library, pretty_print=True)
    LIBRARY = WORKING_DIR + '/' + _con.LIB_FOLDER + '/' + _con.LIB_XML 
    _iof.Write_XML(xml_block, LIBRARY)