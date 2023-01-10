import sys, os
import shutil
from lib_gen import _edx_consts
import __SETTINGS__

#--------------------------------------------------------------------------------------------------
# Text strings
WARNING = "      WARNING:"

#--------------------------------------------------------------------------------------------------
# copy policies to the correct folder
def copyPolicies(library_filename):

    # create the subfolder in the policies folder
    policy_subfolder = os.path.join(sys.argv[2], _edx_consts.POLICIES_FOLDER, library_filename)
    os.mkdir(policy_subfolder)

    # policy.json
    input_policy_filepath = os.path.join(sys.argv[1], _edx_consts.POLICY_FILENAME)
    output_policy_filepath = os.path.join(policy_subfolder, _edx_consts.POLICY_FILENAME)
    if os.path.exists(input_policy_filepath):
        shutil.copyfile(input_policy_filepath, output_policy_filepath)
    else:
        print(WARNING, 'The policy file was not found: ', _edx_consts.POLICY_FILENAME)
