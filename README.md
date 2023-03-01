# lib-gen

A Python3 script for generating an edX library from markdown.

The aim is:
- to allow all library content for checkbox problems to be created using a simple text editor.
- to allow Git version control when developing and reviewing the content.
- to allow easier control over formatting and styles.

The basic workflow is creating a markdown file `name.md` locally in a specific format (see __Format Description__). Then, when you run the python script, its final output is a compressed archive file `library-name.tar.gz` file, that can be directly imported into an edX library. As a by-product, the converted HTML file `name.html` and the XML file `name.xml` are also in the output folder. When the `library-name.tar.gz` file is imported, it will automatically populate the library content on the edX platform.

In addition to the markdown input file, a config file, `config.json`, is also needed to define the input and output filenames and XML tags for the library.xml file. 

```markdown
{
    "INP_MARKDOWN":     "<name>.md",
    "OUT_HTML":         "<name>.html",
    "OUT_XML":          "<name>.xml",
    "DISPLAY_NAME":     "<name> Exam",   
    "LIBRARY":          "<name>XLib",  
    "ORG":              "Exoscale"
}
``` 

>NOTE: existing library content will be overwritten.


## Executing the `lib-gen.py` Script

Running the Python script `lib-gen.py` generates all the edX files comprising the library, including the `libray-name.tar.gz` file for the library import into edX.

Executing the generator:

```
python3 lib-gen.py name
```

The `name` argument in the script call defines only the name part in the `library-name.tar.gz` archive, it should be the same as the `<name>` in the `config.json` file, but it does not have to be.

>NOTE: any existing content in the folders `output` and `library` will be deleted. In addition, the `library-name.tar.gz` will also be deleted in case of a re-run of the script.


## Uploading the `library-name.tar.gz` File

After running the lib-gen script (assuming no errors), a `library-name.tar.gz` file will be generated locally. This file can be uploaded to the edX platform.

>NOTE: When you import the `library-name.tar.gz` file to edX, any existing library content in this edX library will be deleted.


## Format Description `*.md` input file

The markdown input format for the edX library creation containing all the exam checkbox problems is pretty simple:
* Level 1 `#` heading format defines the name of the checkbox problem.
* Level 2 `##` heading format defines the checkbox problem question.
* Paragraphs with leading `[ ]` for wrong answers.
* Paragraphs with leading `[x]` for right answers.
* Answer counts should range from `2` to `8`.
* Paragraph with only `===` defines the end of the checkbox problem.

>NOTE: `[x]` needs to be a small caps `x`


```markdown
# BASICS

## What does the CIDR notation `1.1.1.1/0` mean in a firewall rule?

[ ] All IP addresses starting with `1.1.1` are allowed.

[ ] Only the IP `1.1.1.1` is allowed.

[x] The whole internet is allowed.

[ ] Nothing is allowed.

[ ] The notation is incorrect.

===

# BASICS

##  What is an IP address? 

[x] A numerical label assigned to each device connected to a computer network that uses the Internet Protocol.

[ ] An identifier both for the host and the host's location.

===

```