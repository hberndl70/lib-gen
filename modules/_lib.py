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
        CBP_FILENAME = str(_con.CBP_XML) + str(i)
        problem = etree.SubElement(library, 'problem')
        problem.set ("url_name", CBP_FILENAME )
        i += 1

    xml_block = etree.tostring(library, pretty_print=True)
    LIBRARY = _iof.Working_DIR() + '/' + _con.LIB_FOLDER + '/' + _con.LIB_XML 
    _iof.Write_XML(xml_block, LIBRARY)