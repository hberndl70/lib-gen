#---------------------------------------------------------------
# checkbox problem XML templates
#---------------------------------------------------------------
# building the XML structure for the checkbox problems based on 
# the number of answer options [2 - 8] plus helper function to 
# keep the code more readable and maintanable 
#---------------------------------------------------------------
from lxml import etree
from lxml.builder import E
from modules import _con

def Display_Name(v):
    return {'display_name': v}

def Markdown(v):
    return {'markdown': v}

def Max_Attempts(v):
    return {'max_attempts': v}

def Show_Reset_Button(v):
    return {'show_reset_button': v}

def ShowAnswer(v):
    return {'showanswer': v}

def Weight(v):
    return {'weight': v}

def Correct_Tag(v):
    correct_txt = 'correct=' + '"' + v + '"' + '>'
    return correct_txt

def Check_RoW(v):
    if v[0:3] == '[ ]':
        return 'false'
    else:
        return 'true'

def Build_Label(txt_lbl):
    txt_label = _con.LAB_OPEN + txt_lbl + _con.LAB_CLOSE
    return txt_label

def Build_Choice(txt_ch, right_or_wrong):
    txt_choice = _con.CHO_OPEN + Correct_Tag(right_or_wrong) + txt_ch + _con.CHO_CLOSE
    return txt_choice

def Block_2(disp_name, txt_lbl, txt_ch1, txt_ch2):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    block2 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(_con.DESCRIPTION_TXT),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2))
                )
            ),
            Display_Name(disp_name),
            Markdown('null'),
            Max_Attempts('1'),
            Show_Reset_Button('false'),
            ShowAnswer('never'),
            Weight('1.0')
        )
    )
    xml_block = etree.tostring(block2, pretty_print=True)
    return xml_block 
    
def Block_3(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    block3 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(_con.DESCRIPTION_TXT),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3))
                )
            ),
            Display_Name(disp_name),
            Markdown('null'),
            Max_Attempts('1'),
            Show_Reset_Button('false'),
            ShowAnswer('never'),
            Weight('1.0')
        )
    )
    xml_block = etree.tostring(block3, pretty_print=True)
    return xml_block 

def Block_4(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3, txt_ch4):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    row_ch4 = Check_RoW(txt_ch4)  
    block4 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(_con.DESCRIPTION_TXT),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4))
                )
            ),
            Display_Name(disp_name),
            Markdown('null'),
            Max_Attempts('1'),
            Show_Reset_Button('false'),
            ShowAnswer('never'),
            Weight('1.0')
        )
    )
    xml_block = etree.tostring(block4, pretty_print=True)
    return xml_block 

def Block_5(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    row_ch4 = Check_RoW(txt_ch4)
    row_ch5 = Check_RoW(txt_ch5)
    block5 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(_con.DESCRIPTION_TXT),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4)),
                etree.XML(Build_Choice(txt_ch5[4:], row_ch5))
                )
            ),
            Display_Name(disp_name),
            Markdown('null'),
            Max_Attempts('1'),
            Show_Reset_Button('false'),
            ShowAnswer('never'),
            Weight('1.0')
        )
    )
    xml_block = etree.tostring(block5, pretty_print=True)
    return xml_block 

def Block_6(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5, txt_ch6):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    row_ch4 = Check_RoW(txt_ch4)
    row_ch5 = Check_RoW(txt_ch5)
    row_ch6 = Check_RoW(txt_ch6)
    block6 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(_con.DESCRIPTION_TXT),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4)),
                etree.XML(Build_Choice(txt_ch5[4:], row_ch5)),
                etree.XML(Build_Choice(txt_ch6[4:], row_ch6))                
                )
            ),
            Display_Name(disp_name),
            Markdown('null'),
            Max_Attempts('1'),
            Show_Reset_Button('false'),
            ShowAnswer('never'),
            Weight('1.0')
        )
    )
    xml_block = etree.tostring(block6, pretty_print=True)
    return xml_block 

def Block_7(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5, txt_ch6, txt_ch7):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    row_ch4 = Check_RoW(txt_ch4)
    row_ch5 = Check_RoW(txt_ch5)
    row_ch6 = Check_RoW(txt_ch6)
    row_ch7 = Check_RoW(txt_ch7)
    block7 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(_con.DESCRIPTION_TXT),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4)),
                etree.XML(Build_Choice(txt_ch5[4:], row_ch5)),
                etree.XML(Build_Choice(txt_ch6[4:], row_ch6)),
                etree.XML(Build_Choice(txt_ch7[4:], row_ch7))                
                )
            ),
            Display_Name(disp_name),
            Markdown('null'),
            Max_Attempts('1'),
            Show_Reset_Button('false'),
            ShowAnswer('never'),
            Weight('1.0')
        )
    )
    xml_block = etree.tostring(block7, pretty_print=True)
    return xml_block 

def Block_8(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5, txt_ch6, txt_ch7, txt_ch8):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    row_ch4 = Check_RoW(txt_ch4)
    row_ch5 = Check_RoW(txt_ch5)
    row_ch6 = Check_RoW(txt_ch6)
    row_ch7 = Check_RoW(txt_ch7)
    row_ch8 = Check_RoW(txt_ch8)
    block8 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(_con.DESCRIPTION_TXT),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4)),
                etree.XML(Build_Choice(txt_ch5[4:], row_ch5)),
                etree.XML(Build_Choice(txt_ch6[4:], row_ch6)),
                etree.XML(Build_Choice(txt_ch7[4:], row_ch7)),
                etree.XML(Build_Choice(txt_ch8[4:], row_ch8))   
                )
            ),
            Display_Name(disp_name),
            Markdown('null'),
            Max_Attempts('1'),
            Show_Reset_Button('false'),
            ShowAnswer('never'),
            Weight('1.0')
        )
    )
    xml_block = etree.tostring(block8, pretty_print=True)
    return xml_block 