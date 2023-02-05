# --------------------------------------------------------------
# file I/O for HTML/XML to/from disk
# --------------------------------------------------------------
import os
import subprocess

# --------------------------------------------------------------
# get the corrent working directory 
# --------------------------------------------------------------
def Working_DIR():
	working_dir = os.getcwd()
	return working_dir

# --------------------------------------------------------------
# create a folder 
# --------------------------------------------------------------
def Create_DIR(path):
	os.mkdir(path)

# --------------------------------------------------------------
# delete a folder
# --------------------------------------------------------------
def Delete_DIR(path):
	if os.path.exists(path):
		subprocess.run(["rm", "-rf", path])
	else:
		print('path ' + path + 'do not exist!')

# --------------------------------------------------------------
# copy policy file (assets.json) into the policies folder
# --------------------------------------------------------------
def Copy_POL(file, path):
	if os.path.exists(path):
		subprocess.run(["cp", file, path])
	else:
		print('path ' + path + 'do not exist!')
		
# --------------------------------------------------------------
# read HTML from file
# --------------------------------------------------------------
# functions takes a filename for the HTML input
# and reads it into a string (html_text) which 
# is returned by the function
# --------------------------------------------------------------
def Read_HTML(html_file):
	f = open(html_file, 'r', encoding='utf-8')
	html_read = f.read()
	return html_read

# --------------------------------------------------------------
# write HTML to file
# --------------------------------------------------------------
# functions takes a string with the HTML text and 
# a filename for writing the HTML text to a file on the disk 
# --------------------------------------------------------------
def Write_HTML(html_text, html_file):
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_text)

# --------------------------------------------------------------
# write XML to file
# --------------------------------------------------------------
# functions takes a string with the XML text and 
# a filename for writing the XML text to a file on the disk 
# --------------------------------------------------------------
def Write_XML(xml_text, xml_file):
	with open(xml_file, 'ab') as f:
		f.write(xml_text)
