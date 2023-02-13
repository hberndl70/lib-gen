#------------------------------------------------------------------------------
# CONSTANT definitions for m2x converter
#------------------------------------------------------------------------------

# Folder names for input / output
#------------------------------------------------------------------------------
INP_FOLDER      = 'input'
OUT_FOLDER      = 'output'

# Folder names for writing xml file
#------------------------------------------------------------------------------
LIB_FOLDER      = 'library'    

# library.xml configuration
#------------------------------------------------------------------------------
URL_NAME        = 'library'
XBLOCK_FAMILY   = 'xblock.v1'
ORG             = 'Exoscale'
#------------------------------------------------------------------------------
DISPLAY_NAME    = 'ADVANCED Exam'                # <-- value form config.json or cli parameter
LIBRARY         = 'AdvancedXLib'                 # <-- value form config.json or cli parameter
 
# Folder names for writing xml components
#------------------------------------------------------------------------------
PRO_FOLDER      = 'problem'

# Folder for policies
#------------------------------------------------------------------------------
POL_FOLDER      = 'policies'
POL_FILENAME    = 'assets.json'

# XML constants for block creation
#------------------------------------------------------------------------------
LAB_OPEN        = '<p>'
LAB_CLOSE       = '</p>'

CHO_OPEN        = '<choice '
CHO_CLOSE       = '</choice>'

DES_TEXT        = 'Please select all applicable options from the list below. Multiple selections are allowed.'

# File name for the library and the checkbox problem definition .xml files
#------------------------------------------------------------------------------
LIB_XML         ='library.xml'                          # moocit expects a library.xml file in the tar.gz archive
CBP_XML         ='00000000000000000000000000000000'     # checkbox probleme filenames are 32 characters long

# File names for output files TESTING
#------------------------------------------------------------------------------
OUT_HTM        = 'test.html'                # = filename without extension (from cli parameter) + '.html'
OUT_XML        = 'test.xml'                 # = filename without extension (from cli parameter) + '.xml'   

# File name for input files TESTING 
#------------------------------------------------------------------------------
INP_MD         = 'test.md'                  # = filename from cli parameter 