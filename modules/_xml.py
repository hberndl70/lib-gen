from lxml import etree
from lxml.builder import E
from modules import _iof

LABEL_OPEN      = '<p>'
LABEL_CLOSE     = '</p>'
DESCRIPTION     = 'Please select all applicable options from the list below. Multiple selections are allowed.'
CHOICE_OPEN     = '<choice '
CHOICE_CLOSE    = '</choice>'

FILE_XML = "/Users/hansberndl/_tst/md2xml/output/test.xml"
xml_file      = "" + FILE_XML

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
        return "false"
    else:
        return "true"

def Build_Label(txt_lbl):
    txt_label = LABEL_OPEN + txt_lbl + LABEL_CLOSE
    return txt_label

def Build_Choice(txt_ch, right_or_wrong):
    txt_choice = CHOICE_OPEN + Correct_Tag(right_or_wrong) + txt_ch + CHOICE_CLOSE
    return txt_choice

def Block_2(disp_name, txt_lbl, txt_ch1, txt_ch2):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    block2 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(DESCRIPTION),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2))
                )
            ),
            Display_Name(disp_name),
            Markdown("null"),
            Max_Attempts("1"),
            Show_Reset_Button("false"),
            ShowAnswer("never"),
            Weight("1.0")
        )
    )
    etree.dump(block2)
    xml_block = etree.tostring(block2, pretty_print=True)
    _iof.Write_XML(xml_block, xml_file)
    
def Block_3(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    block3 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(DESCRIPTION),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3))
                )
            ),
            Display_Name(disp_name),
            Markdown("null"),
            Max_Attempts("1"),
            Show_Reset_Button("false"),
            ShowAnswer("never"),
            Weight("1.0")
        )
    )
    etree.dump(block3)
    xml_block = etree.tostring(block3, pretty_print=True)
    _iof.Write_XML(xml_block, xml_file)

def Block_4(disp_name, txt_lbl, txt_ch1, txt_ch2, txt_ch3, txt_ch4):
    row_ch1 = Check_RoW(txt_ch1)
    row_ch2 = Check_RoW(txt_ch2)
    row_ch3 = Check_RoW(txt_ch3)
    row_ch4 = Check_RoW(txt_ch4)  
    block4 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(Build_Label(txt_lbl))), 
            E.description(DESCRIPTION),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4))
                )
            ),
            Display_Name(disp_name),
            Markdown("null"),
            Max_Attempts("1"),
            Show_Reset_Button("false"),
            ShowAnswer("never"),
            Weight("1.0")
        )
    )
    etree.dump(block4)
    xml_block = etree.tostring(block4, pretty_print=True)
    _iof.Write_XML(xml_block, xml_file)

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
            E.description(DESCRIPTION),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4)),
                etree.XML(Build_Choice(txt_ch5[4:], row_ch5))
                )
            ),
            Display_Name(disp_name),
            Markdown("null"),
            Max_Attempts("1"),
            Show_Reset_Button("false"),
            ShowAnswer("never"),
            Weight("1.0")
        )
    )
    etree.dump(block5)
    xml_block = etree.tostring(block5, pretty_print=True)
    _iof.Write_XML(xml_block, xml_file)

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
            E.description(DESCRIPTION),
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
            Markdown("null"),
            Max_Attempts("1"),
            Show_Reset_Button("false"),
            ShowAnswer("never"),
            Weight("1.0")
        )
    )
    etree.dump(block6)
    xml_block = etree.tostring(block6, pretty_print=True)
    _iof.Write_XML(xml_block, xml_file)

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
            E.description(DESCRIPTION),
            E.checkboxgroup(
                etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),
                etree.XML(Build_Choice(txt_ch2[4:], row_ch2)),
                etree.XML(Build_Choice(txt_ch3[4:], row_ch3)),
                etree.XML(Build_Choice(txt_ch4[4:], row_ch4)),
                etree.XML(Build_Choice(txt_ch5[4:], row_ch5)),
                etree.XML(Build_Choice(txt_ch5[4:], row_ch6)),
                etree.XML(Build_Choice(txt_ch6[4:], row_ch7))                
                )
            ),
            Display_Name(disp_name),
            Markdown("null"),
            Max_Attempts("1"),
            Show_Reset_Button("false"),
            ShowAnswer("never"),
            Weight("1.0")
        )
    )
    etree.dump(block7)
    xml_block = etree.tostring(block7, pretty_print=True)
    _iof.Write_XML(xml_block, xml_file)

# def Block_2(disp_name, txt_lbl, txt_ch1, txt_ch2):
#     row_ch1 = Check_RoW(txt_ch1)      <-- checking for the choice value [ ] = "false" [x] = "true"
#     row_ch2 = Check_RoW(txt_ch2)      <-- checking for the choice value [ ] = "false" [x] = "true"
#     block2 = (
#         E.problem(
#             E.choiceresponse(
#             E.label(etree.XML(Build_Label(txt_lbl))), 
#             E.description(DESCRIPTION),
#             E.checkboxgroup(
#                 etree.XML(Build_Choice(txt_ch1[4:], row_ch1)),    <-- txt_ch1[4:] = removing [ ] or [x] from the string 
#                 etree.XML(Build_Choice(txt_ch2[4:], row_ch2))     <-- txt_ch1[4:] = removing [ ] or [x] from the string 
#                 )
#             ),
#             Display_Name(disp_name),
#             Markdown("null"),
#             Max_Attempts("1"),
#             Show_Reset_Button("false"),
#             ShowAnswer("never"),
#             Weight("1.0")
#         )
#     )
#     etree.dump(block2)