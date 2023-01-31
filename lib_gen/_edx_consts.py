#--------------------------------------------------------------------------------------------------
# Folders

# Folder names for writing output
LIB_FOLDER              = "library"         # library folder

# Folder names for writing components
COMP_PROBS_FOLDER       = "problem"

# Folder for policies
POLICIES_FOLDER         = "policies"
POLICY_FILENAME         = "assets.json"


#--------------------------------------------------------------------------------------------------
# Metadata settings for folders

# root
ROOT_FOLDER_REQ         = ['org', 'course', 'url_name']
ROOT_FOLDER_OPT         = ['visible_to_staff_only', 'start']

# library
LIB_FOLDER_REQ          = ['display_name']
LIB_FOLDER_OPT          = ['visible_to_staff_only', 'enrollment_start', 'start', 'end', 'self_paced', 'is_new', 'cert_html_view_enabled', 'course_image', 'graceperiod', 'instructor_info', 'invitation_only', 'language', 'learning_info', 'minimum_grade_credit', 'wiki_slug', 'cosmetic_display_price']

# component
COMP_FOLDER_REQ         = ['display_name']
COMP_FOLDER_OPT         = ['visible_to_staff_only', 'start']


#--------------------------------------------------------------------------------------------------
# Metadata settings for components

COMP_PROB_QUIZ_REQ      = ['type']
COMP_PROB_QUIZ_OPT      = ['display_name', 'visible_to_staff_only', 'id', 'verified_only', 'start', 'max_attempts', 'weight', 'showanswer', 'group_access', 'rerandomize', 'attempts_before_showanswer_button']


#--------------------------------------------------------------------------------------------------
# Metadata settings for components

METADATA_ENUMS          = {

    'visible_to_staff_only':    ['true', 'false'],

    # settings files

    'hide_after_due':           ['true', 'false'],
    'graded':                   ['true', 'false'],
    'invitation_only':          ['true', 'false'],
    'cert_html_view_enabled':   ['true', 'false'],

    # component files

    'download_video':           ['true', 'false'],
    'show_reset':               ['true', 'false'],
    'show_captions':            ['true', 'false'],
    'type':                     ['html', 'video', 'problem-checkboxes'],
    'rerandomize':              ["always", "never", "onreset", "per_student"],
    'showanswer':               ["always", "never", "answered", "attempted", "closed", "finished", "past_due", "correct_or_past_due", "after_attempts"]
}

#--------------------------------------------------------------------------------------------------
MD_SNIPPET_MARKERS      = ['# ROOT', '# MOOC', '# LIBRARY', '# PROBLEM-CHECKBOX']
#--------------------------------------------------------------------------------------------------
