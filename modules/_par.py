#---------------------------------------------------------------
# parsing HTML and splitting in components (strings) 
#---------------------------------------------------------------
# parsing the converted markdown input (Conv_Markdown) and split 
# it into information components (Parse_HMTL) then used to build 
# the seperate XML files describing the checkbox problems.
#---------------------------------------------------------------
import re
import markdown
from bs4 import BeautifulSoup
from modules import _con
from modules import _iof
from modules import _lib
from modules import _xml

#---------------------------------------------------------------
# pre parsing checks
#---------------------------------------------------------------
def Check_Box(box):
    if box == 0:
        print('... boxes OK!')
        check_boxes = True
    else:
        print('... boxes ERROR!')
        check_boxes =False
    return check_boxes

def Check_Format(h1, h2, eop):
    # check of structural integrity 
    if h1 == h2 == eop:
        print('... format OK!')
        check_format = True
    else:
        print('... format ERROR!')
        check_format = False
    return check_format

def Check_Blanks(h1, h2, eop, cbp, nl):
    # check of blank lines integrity 
    if h1 + h2 + eop + cbp - nl == 0:
        print('... blanks OK!')
        check_blanks = True
    else:
        print('... blanks ERROR!')
        check_blanks = False
    return check_blanks

def Check_Markdown(input_file):
    with open(input_file, 'r') as f:
        text = f.read()

    # find all markdown header - level 1 = number of Check Box Problems 
    h1 = len(re.findall('^# |[^#]# ', text))
    # find all markdown header - level 2 = number of Check Box Problem Questions
    h2 = len(re.findall('[#]# ', text))
    #find all === end of problem markers 
    eop = len(re.findall('===', text))
    # find all [ ] or [x] answer  = check Box Problem Answers 
    cbp = len(re.findall('\[[ x]\]', text))
    box = len(re.findall('\[[X]\]', text))
    # find all New Lines = check for right amount of blank lines 
    nl = len(re.findall('[/\n]{2}', text))

    # if there is a boxes problem ... terminate
    if not Check_Box(box):
        return False
        
    # if there is a format problem ... terminate
    if not Check_Format(h1, h2, eop):                      
        return False 
  
    # if there is a blanks problem ... terminate
    if not Check_Blanks(h1, h2, eop, cbp, nl) :
        return False
    return True

#---------------------------------------------------------------

def Conv_Markdown(input_file):
    with open(input_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
    return html

def Conv_List(txt):
    # convert bs4 list of strings into one string
    append = ''.join(map(str,txt))
    return append

def Build_XML(template, block, cbp_num, cbp_folder, xml_file):
    match template:
        case 1:
            print('A one answer knowledge check does not make sense ...')
        case 2:
            xml_block = _xml.Block_2(block[0], block[1], block[2], block[3])
        case 3:
            xml_block = _xml.Block_3(block[0], block[1], block[2], block[3], block[4])
        case 4:
            xml_block = _xml.Block_4(block[0], block[1], block[2], block[3], block[4], block[5])
        case 5:
            xml_block = _xml.Block_5(block[0], block[1], block[2], block[3], block[4], block[5], block[6])
        case 6:
            xml_block = _xml.Block_6(block[0], block[1], block[2], block[3], block[4], block[5], block[6], block[7])
        case 7:
            xml_block = _xml.Block_7(block[0], block[1], block[2], block[3], block[4], block[5], block[6], block[7], block[8])
        case 8:
            xml_block = _xml.Block_8(block[0], block[1], block[2], block[3], block[4], block[5], block[6], block[7], block[8], block[9])    
        case _:
            print('...something went wrong, to many answers or other errors, check your *.md input file.')
            
    CBP_FILENAME = cbp_folder + '/' + _iof.Create_Name32(str(_con.CBP_XML), str(cbp_num)) + '.xml'
    _iof.Write_CBP(xml_block, CBP_FILENAME)     # writing problem file e.g. <00000..00001.xml> into problem folder
    _iof.Write_XML(xml_block, xml_file)         # writing xml structure to the test.xml control file
    
def Parse_HTML(html_text, xml_file, cbp_folder):
    #---------------------------------------------------------------
    # fetch the html character soup ;)
    #---------------------------------------------------------------
    soup = BeautifulSoup(html_text, "html.parser")
    #---------------------------------------------------------------
    # get all list of strings for
    # checkbox problem names, questions, answers 
    #---------------------------------------------------------------
    display  = soup.find_all('h1')
    label    = soup.find_all('h2')
    answers  = soup.find_all('p')
    #---------------------------------------------------------------
    # init number of questions in the input file
    #---------------------------------------------------------------
    cbp_num = len(display)
    #---------------------------------------------------------------
    # create library.xml file in the folder structure
    #---------------------------------------------------------------
    print('writing xml ...')
    _lib.Write_LIB_XML(cbp_num)
    #---------------------------------------------------------------
    # init strings for checkbox problem names, question, answers
    #---------------------------------------------------------------
    cbp_str1 = ''
    cbp_str2 = ''
    cbp_str3 = ''
    #---------------------------------------------------------------
    # init list of strings (kc) for xml_block generation
    #---------------------------------------------------------------
    cbp_list = []
    #---------------------------------------------------------------
    # init counters for loop control
    #---------------------------------------------------------------
    tem_select  = 0   # template selector (Block_2, Block_3, ...)
    ans_index   = 0   # answer index
    cbp_counter = 0   # checkbox problem counter

    while cbp_counter < cbp_num:
        cbp_str1 = display[cbp_counter].text
        cbp_str2 = label[cbp_counter].contents
        cbp_list.append(cbp_str1)
        cbp_list.append(Conv_List(cbp_str2))
        cbp_counter += 1

        while  answers[ans_index].text != '===':
            cbp_str3 = answers[ans_index].contents
            cbp_list.append(Conv_List(cbp_str3))
            tem_select += 1
            ans_index  += 1

        Build_XML(tem_select, cbp_list, cbp_counter, cbp_folder, xml_file)
    
        # reset for next checkbox problem block parsing
        cbp_list    = []
        cbp_str1    = ''
        cbp_str2    = ''    
        cbp_str3    = ''
        tem_select  = 0     # reset the template selector
        ans_index  += 1     # increase index to process the next answers block 
