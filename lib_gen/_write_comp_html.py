import sys, os
from lxml import etree
from lib_gen import  _edx_consts
from lib_gen import  _process_html
from lib_gen import  _css_settings
import __SETTINGS__

#--------------------------------------------------------------------------------------------------
# write xml for Html component
def writeXmlForHtmlComp(component_path, filename, content, settings, unit_filename):

    # ---- Html file in COMP_HTML_FOLDER----
    # <p>
    #   <span style="text-decoration: underline;">Objective:</span>
    # </p>
    # <p>
    #   This week's assignment is broken down into <strong>three file submissions</strong>. 
    #   These smaller submissions are meant to help you along the way.
    # </p>
    # <p>
    #   <img height="288" width="498" src="/static/assignment.png" alt="" 
    #   style="display: block; margin-left: auto; margin-right: auto;" />
    # </p>
    # ----  ----  ----

    # ---- XML file in COMP_HTML_FOLDER----
    # <html 
    #   filename="xxx" 
    #   display_name="Task" 
    #   editor="visual"
    # />
    # ----  ----  ----

    # process html
    _process_html.processHtmlTags(component_path, content, unit_filename)

    # write the html file
    html_out_path = os.path.join(sys.argv[2], _edx_consts.COMP_HTML_FOLDER, filename + '.html')
    with open(html_out_path, 'wb') as fout:
        if 'display_name' in  settings:
            h3_tag = etree.Element("h3")
            h3_tag.text = settings['display_name']
            h3_tag.set('style', _css_settings.H3_CSS)
            fout.write(etree.tostring(h3_tag, pretty_print = True))
        for tag in content:
            tag_result = etree.tostring(tag, pretty_print = True, method = "html")
            fout.write(tag_result)

    # create xml
    html_tag = etree.Element("html")
    for key in settings:
        if key not in ['type']:
            html_tag.set(key, settings[key])
    html_tag.set('filename', filename)
    result = etree.tostring(html_tag, pretty_print = True)

    # write the xml file to COMP_HTML_FOLDER
    xml_out_path = os.path.join(sys.argv[2], _edx_consts.COMP_HTML_FOLDER, filename + '.xml')
    with open(xml_out_path, 'wb') as fout:
        fout.write(result)

    # return the file name and folder
    return [
        [filename, _edx_consts.COMP_HTML_FOLDER]
    ]
    
#--------------------------------------------------------------------------------------------------
