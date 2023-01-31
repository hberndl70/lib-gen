# --------------------------------------------------------------
# file IO for HTML/XML to/from disk
# --------------------------------------------------------------
from lxml import html
from lxml import etree

# --------------------------------------------------------------
# read HTML from file
# --------------------------------------------------------------
# functions takes a filename for the HTML input
# and reads it into a string (html_text) which 
# is returned by the function
# --------------------------------------------------------------
def read_html(html_file):
	with open(html_file, 'r', encoding='utf-8') as inp:
		html_text = html.fromstring(inp.read())
	return html_text

# --------------------------------------------------------------
# write HTML to file
# --------------------------------------------------------------
# functions takes a string with the HTML text and 
# a filename for writing the HTML text to a file on the disk 
# --------------------------------------------------------------
def write_html(html_text, html_file):
    with open(html_file, 'w') as f:
        f.write(html_text)

# --------------------------------------------------------------
# write XML to file
# --------------------------------------------------------------
# functions takes a string with the XML text and 
# a filename for writing the XML text to a file on the disk 
# --------------------------------------------------------------
def write_xml(xml_text, xml_file):
	with open(xml_file, 'wb') as out:
		out.write(etree.tostring(xml_text))

