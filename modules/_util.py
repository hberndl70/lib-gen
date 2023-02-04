import os
# import __SETTINGS__

#--------------------------------------------------------------------------------------------------
# get all the sub folders in a folder
# return the folder names and folder paths, like this 
# [[folder_name, folder_path], [folder_name, folder_path], [folder_name, folder_path]...]
def getSubFolders(folder_path):
    folders = []
    files_and_folders = os.listdir(folder_path)
    for file_or_folder in files_and_folders:
        path = os.path.join(folder_path, file_or_folder)
        if (not os.path.isfile(path)):
            folders.append([file_or_folder, path])
    folders.sort()
    return folders
    
#--------------------------------------------------------------------------------------------------
# get all the files in a folder
# return a list of file names and file paths, as a pair
# [[file_name, file_path], [file_name, file_path], [file_name, file_path] ...]
def getFiles(folder_path):
    files = []
    files_and_folders = os.listdir(folder_path)
    for file_or_folder in files_and_folders:
        path = os.path.join(folder_path, file_or_folder)
        if (os.path.isfile(path)):
            files.append([file_or_folder, path])
    files.sort()
    return files

#--------------------------------------------------------------------------------------------------
# check if the text starts with any of the strings in the list
def starts(text, starts_list):
    for start in starts_list:
        if text.startswith(start):
            return True
    return False

#--------------------------------------------------------------------------------------------------
# check if the text ends with any of the strings in the list
def ends(text, ends_list):
    for end in ends_list:
        if text.endswith(end):
            return True
    return False
    
#--------------------------------------------------------------------------------------------------
