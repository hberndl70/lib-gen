# --------------------------------------------------------------
# parsing HTML and splitting in components (strings) 
# --------------------------------------------------------------
# parsing the converted markdown input (Conv_Markdown) and 
# split it into information componets (Parse_HMTL) then used to 
# build the library.xml and the problem defnitions in XML stored 
# in the problem folder.
# (000000000000000000001.xml, 000000000000000000002.xml, ...)  
# --------------------------------------------------------------
import markdown
from bs4 import BeautifulSoup
from modules import _xml

def Conv_Markdown(input_file):
    with open(input_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return html

def Conv_List(txt):
    # convert bs4 list of strings into one string
    append = ' '.join(map(str,txt))
    return append

def Build_XML(block, template):
    match template:
        case 1:
            print('A one answer knowledge check does not make sense ...')
        case 2:
            _xml.Block_2(block[0], block[1], block[2], block[3])
        case 3:
            _xml.Block_3(block[0], block[1], block[2], block[3], block[4])
        case 4:
            _xml.Block_4(block[0], block[1], block[2], block[3], block[4], block[5])
        case 5:
            _xml.Block_5(block[0], block[1], block[2], block[3], block[4], block[5], block[6])
        case 6:
            _xml.Block_6(block[0], block[1], block[2], block[3], block[4], block[5], block[6], block[7])
        case 7:
            _xml.Block_7(block[0], block[1], block[2], block[3], block[4], block[5], block[6], block[7], block[8])
        case _:
            print('...something went wrong, to many answers or other errors, check your *.md input file.')

def Parse_HTML(html_text):
    # --------------------------------------------------------------
    # fetch the html character soup ;)
    # --------------------------------------------------------------
    soup = BeautifulSoup(html_text, "html.parser")
    # --------------------------------------------------------------
    # get all list of strings for
    # checkbox problem names, questions, answers 
    # --------------------------------------------------------------
    display  = soup.find_all('h1')
    label    = soup.find_all('h2')
    answers  = soup.find_all('p')
    # --------------------------------------------------------------
    # init number of questions in the input file
    # --------------------------------------------------------------
    num_q = len(display)
    # --------------------------------------------------------------
    # init strings for checkbox problem names, question, answers
    # -------------------------------------------------------------- 
    kc_str_1 = ''
    kc_str_2 = ''
    kc_str_3 = ''
    # --------------------------------------------------------------
    # init list of strings (kc) for xml_block generation
    # --------------------------------------------------------------
    kc_lst = []
    # --------------------------------------------------------------
    # init counters for loop control
    # --------------------------------------------------------------
    cnt_t = 0   # template selector (Block_2, Block_3, ...)
    cnt_a = 0   # index of answer
    cnt_q = 0   # index of question 

    while cnt_q < num_q:
        kc_str_1 = display[cnt_q].text
        kc_str_2 = label[cnt_q].contents
        kc_lst.append(kc_str_1)
        kc_lst.append(Conv_List(kc_str_2))
        cnt_q += 1

        while  answers[cnt_a].text != '===':
            kc_str_3 = answers[cnt_a].contents
            kc_lst.append(Conv_List(kc_str_3))
            cnt_t += 1
            cnt_a += 1

        print('\n')
        Build_XML(kc_lst, cnt_t)
    
        # reset for next checkbox problem block parsing
        kc_lst   = []
        kc_str_1 = ''
        kc_str_2 = ''    
        kc_str_3 = ''
        cnt_t    = 0
        cnt_a   += 1
