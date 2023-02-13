# --------------------------------------------------------------
# writing the library.xml file
# --------------------------------------------------------------
# this file is the inventory / overview file for the edx library 
# it holds the information for e.g.:
# display_name="xxx" org="yyy" library="zzz" 
# and the list of all library components (problems) 
# 00000000000000000000000000000001, 
# 00000000000000000000000000000002, ...
# stored in the correspondend folder (problem) 
# --------------------------------------------------------------
from lxml import etree
from modules import _con 
from modules import _iof

def Write_LIB_XML(cbp_number):
    library = etree.Element('library')

    library.set ('url_name',      _con.URL_NAME)
    library.set ('xblock-family', _con.XBLOCK_FAMILY)
    library.set ('display_name',  _con.DISPLAY_NAME)
    library.set ('org',           _con.ORG)
    library.set ('library',       _con.LIBRARY)

    i = 1
    while i <= cbp_number:
        CBP_FILENAME = _iof.Create_Name32(str(_con.CBP_XML), str(i))
        problem = etree.SubElement(library, 'problem')
        problem.set ("url_name", CBP_FILENAME )
        i += 1

    xml_block = etree.tostring(library, pretty_print=True)
    LIBRARY = _iof.Working_DIR() + '/' + _con.LIB_FOLDER + '/' + _con.LIB_XML 
    _iof.Write_XML(xml_block, LIBRARY)