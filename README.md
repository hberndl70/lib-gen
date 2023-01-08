# lib-gen

A Python3 script for generating an edX library from markdown.

The aim is:
- to allow all library content to be created using a simple text editor outside the browser.
- to allow Git version control to be used when developing and reviewing the content.
- to allow better control over formatting and styles.

The basic workflow is that you create all your content locally, in a specific file/folder structure. When you run the python script, it generates a compressed `*.tar.gz` file that can be directly imported into a edX library. When this file is imported, it will automatically populate the library content on edX. NOTE: exisiting library content will be overwritten.

## Execution

There is the `lib_generator.py` Python script:
It generates all the edX files which comprise the library, including the `library.<name>.tar.gz` file for the import of the library into edX.

Execute the generator:

```
python ./lib_generator.py ./input/ ./output/
```

The `__SETTINGS__.py` file in the edX course root input folder specifies a set of global settings that you can set for your context. 

**WARNING: any existing contents in the output folder (i.e. in this case `./output/library`) will be deleted.**


## Upload the `*.tar.gz` File

After running the edX generator (assuming no errors), a `library.<name>.tar.gz` file will be generated. This file can be uploaded to the edX platform.

**WARNING: When you upload the `library.<name>.tar.gz` file to edX, any existing library content in this edX library will be deleted.**
