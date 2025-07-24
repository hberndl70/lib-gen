"""
Constants module for lib-gen converter.

This module contains all constant values used throughout the lib-gen application
for converting markdown files to edX library XML format.
"""

from typing import Final

# =============================================================================
# Directory Structure Constants
# =============================================================================

# Input/Output folder names
INPUT_FOLDER: Final[str] = 'input'
OUTPUT_FOLDER: Final[str] = 'output'
LIBRARY_FOLDER: Final[str] = 'library'

# Library subfolder names
PROBLEM_FOLDER: Final[str] = 'problem'
POLICIES_FOLDER: Final[str] = 'policies'

# =============================================================================
# Configuration File Constants
# =============================================================================

CONFIG_FILENAME: Final[str] = 'config.json'
POLICIES_FILENAME: Final[str] = 'assets.json'

# =============================================================================
# edX Library XML Constants
# =============================================================================

# Standard library.xml configuration
LIBRARY_URL_NAME: Final[str] = 'library'
XBLOCK_FAMILY: Final[str] = 'xblock.v1'
LIBRARY_XML_FILENAME: Final[str] = 'library.xml'

# =============================================================================
# Checkbox Problem (CBP) Constants
# =============================================================================

# Standard checkbox problem filename template (32 characters of zeros)
CBP_FILENAME_TEMPLATE: Final[str] = '00000000000000000000000000000000'

# Default problem settings
DEFAULT_MAX_ATTEMPTS: Final[str] = '1'
DEFAULT_WEIGHT: Final[str] = '1.0'
DEFAULT_SHOW_RESET_BUTTON: Final[str] = 'false'
DEFAULT_SHOW_ANSWER: Final[str] = 'never'
DEFAULT_MARKDOWN_VALUE: Final[str] = 'null'

# Problem description text
DEFAULT_DESCRIPTION: Final[str] = (
    'Please select all applicable options from the list below. '
    'Multiple selections are allowed.'
)

# =============================================================================
# HTML/XML Formatting Constants
# =============================================================================

# HTML paragraph tags
PARAGRAPH_OPEN_TAG: Final[str] = '<p>'
PARAGRAPH_CLOSE_TAG: Final[str] = '</p>'

# XML choice tags
CHOICE_OPEN_TAG: Final[str] = '<choice '
CHOICE_CLOSE_TAG: Final[str] = '</choice>'

# =============================================================================
# Markdown Parsing Constants
# =============================================================================

# Markdown checkbox patterns
CHECKBOX_UNCHECKED: Final[str] = '[ ]'
CHECKBOX_CHECKED: Final[str] = '[x]'
PROBLEM_SEPARATOR: Final[str] = '==='

# =============================================================================
# File Extensions
# =============================================================================

MARKDOWN_EXTENSION: Final[str] = '.md'
HTML_EXTENSION: Final[str] = '.html'
XML_EXTENSION: Final[str] = '.xml'
TAR_EXTENSION: Final[str] = '.tar'
GZ_EXTENSION: Final[str] = '.gz'

# =============================================================================
# Archive Constants
# =============================================================================

LIBRARY_ARCHIVE_PREFIX: Final[str] = 'library-'

# =============================================================================
# Legacy Compatibility Constants (for backward compatibility)
# =============================================================================

# Map old constant names to new ones for backward compatibility
INP_FOLDER = INPUT_FOLDER
OUT_FOLDER = OUTPUT_FOLDER
LIB_FOLDER = LIBRARY_FOLDER
PRB_FOLDER = PROBLEM_FOLDER
POL_FOLDER = POLICIES_FOLDER
CFG_FILENAME = CONFIG_FILENAME
POL_FILENAME = POLICIES_FILENAME
URL_NAME = LIBRARY_URL_NAME
LIB_XML = LIBRARY_XML_FILENAME
CBP_XML = CBP_FILENAME_TEMPLATE
DESCRIPTION_TXT = DEFAULT_DESCRIPTION
LAB_OPEN = PARAGRAPH_OPEN_TAG
LAB_CLOSE = PARAGRAPH_CLOSE_TAG
CHO_OPEN = CHOICE_OPEN_TAG
CHO_CLOSE = CHOICE_CLOSE_TAG
