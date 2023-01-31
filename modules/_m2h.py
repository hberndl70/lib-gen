# --------------------------------------------------------------
# markdown to html conversion 
# --------------------------------------------------------------
# functions takes filename (absolute path+filename)
# converts markdown input-text into html output-text
# returns a html string with the conversion result
# --------------------------------------------------------------
import markdown

def conv_md2html(input_file):
    with open(input_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    return html
