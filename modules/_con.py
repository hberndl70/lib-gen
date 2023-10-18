#---------------------------------------------------------------
# CONSTANT definitions - default values for lib generator 
#---------------------------------------------------------------

# Folder names for input / output 
#---------------------------------------------------------------
INP_FOLDER      = 'input'
OUT_FOLDER      = 'output'
CFG_FILENAME    = 'config.json'

# Folder names for writing xml file
#---------------------------------------------------------------
LIB_FOLDER      = 'library'    

# Folder names for writing xml components
#---------------------------------------------------------------
PRB_FOLDER      = 'problem'

# Folder for policies
#---------------------------------------------------------------
POL_FOLDER      = 'policies'
POL_FILENAME    = 'assets.json'

# library.xml standard tag configuration
#---------------------------------------------------------------
URL_NAME        = 'library'
XBLOCK_FAMILY   = 'xblock.v1'

# XML constants for block and filename creation
#---------------------------------------------------------------
LAB_OPEN        = '<p>'
LAB_CLOSE       = '</p>'
CHO_OPEN        = '<choice '
CHO_CLOSE       = '</choice>'
LIB_XML         = 'library.xml'                                 # moocit expects a library.xml in the tar.gz archive
CBP_XML         = '00000000000000000000000000000000'            # checkbox probleme filenames are 32 characters long
DESCRIPTION_TXT = 'Please select all applicable options from the list below. Multiple selections are allowed.'
