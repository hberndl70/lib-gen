# lib-gen

A Python3 script for generating an edX library from markdown.

The aim is:
- to allow all library content for checkbox problems to be created using a simple text editor outside the browser.
- to allow Git version control to be used when developing and reviewing the content.
- to allow better control over formatting and styles.

The basic workflow is that you create a markdown file `name.md` localy, in a specific format (see __Format Description__). When you run the python script, it's final output is a compressed archive file `library-name.tar.gz` file that can be directly imported into a edX library. As a by-product there is also the converted HTML-file `name.html` and the XML-File `name.xml` in the output folder. When the `library-name.tar.gz` file is imported, it will automatically populate the library content on edX. 

>NOTE: exisiting library content will be overwritten.


## Format Description

The markdown input format for the edX library creation containing all the exam checkbox problems is pretty simple:
* Level 1 `#` heading format is used to define the name of the checkbox problem.
* Level 2 `##` heading format is used to define the checkbox problem question.
* Paragraphs with leading `[ ]` for wrong answers and `[x]` for write answers are used to define the checkbox problem answers.
* Paragraph with only `===` defines the end of the checkbox problem.

>NOTE: `[x]` needs to be a small caps `x`

```markdown
# BASICS

## In a firewall rule what does the CIDR notation `1.1.1.1/0` mean?

[ ] All IP addresses starting with `1.1.1` are allowed.

[ ] Only the IP `1.1.1.1` is allowed.

[x] The whole internet is allowed.

[ ] Nothing is allowed.

[ ] The notation is incorrect.

===

# BASICS

##  What is an IP address? 

[x] A numerical label assigned to each device connected to a computer network that uses the Internet Protocol.

[ ] An identifier both for the host and the host’s location.

===
```


## Executing the `lib-gen.py` Script

Running the Python script `lib-gen.py` generates all the edX files which comprise the library, including the `lib-name.tar.gz` file for the import of the library into edX.

Executing the generator:

```
python3 lib-gen.py input_file.md
```

>NOTE: any existing content in the folders `output` and `library` will be deleted.


## Uploading the `library-name.tar.gz` File

After running the lib-gen script (assuming no errors), a `lib-name.tar.gz` file will be generated locally. This file can be uploaded to the edX platform.

>NOTE: When you import the `lib-name.tar.gz` file to edX, any existing library content in this edX library will be deleted.
