from lxml import etree
from lxml.builder import E

CHOICE_OPEN     = '<choice '
CHOICE_CLOSE    = '</choice>'

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

def Correct(v):
    correct_txt = 'correct=' + '"' + v + '"' + '>'
    return correct_txt

def Build_Choice(txt_parse, corr_val):
    txt_choice = CHOICE_OPEN + Correct(corr_val) + txt_parse + CHOICE_CLOSE
    return txt_choice

def XML_Block_2(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2):
    xml_block2 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(txt_lbl)), 
            E.description(txt_desc),
            E.checkboxgroup(
                etree.XML(txt_ch1),
                etree.XML(txt_ch2)
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
    etree.dump(xml_block2)

def XML_Block_3(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2, txt_ch3):
    xml_block3 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(txt_lbl)), 
            E.description(txt_desc),
            E.checkboxgroup(
                etree.XML(txt_ch1),
                etree.XML(txt_ch2),
                etree.XML(txt_ch3)
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
    etree.dump(xml_block3)

def XML_Block_4(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2, txt_ch3, txt_ch4):
    xml_block4 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(txt_lbl)), 
            E.description(txt_desc),
            E.checkboxgroup(
                etree.XML(txt_ch1),
                etree.XML(txt_ch2),
                etree.XML(txt_ch3),
                etree.XML(txt_ch4)
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
    etree.dump(xml_block4)

def XML_Block_5(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5):
    xml_block5 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(txt_lbl)), 
            E.description(txt_desc),
            E.checkboxgroup(
                etree.XML(txt_ch1),
                etree.XML(txt_ch2),
                etree.XML(txt_ch3),
                etree.XML(txt_ch4),
                etree.XML(txt_ch5)
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
    etree.dump(xml_block5)

def XML_Block_6(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5, txt_ch6):
    xml_block6 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(txt_lbl)), 
            E.description(txt_desc),
            E.checkboxgroup(
                etree.XML(txt_ch1),
                etree.XML(txt_ch2),
                etree.XML(txt_ch3),
                etree.XML(txt_ch4),
                etree.XML(txt_ch5),
                etree.XML(txt_ch6)
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
    etree.dump(xml_block6)

def XML_Block_7(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5, txt_ch6, txt_ch7):
    xml_block7 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(txt_lbl)), 
            E.description(txt_desc),
            E.checkboxgroup(
                etree.XML(txt_ch1),
                etree.XML(txt_ch2),
                etree.XML(txt_ch3),
                etree.XML(txt_ch4),
                etree.XML(txt_ch5),
                etree.XML(txt_ch6),
                etree.XML(txt_ch7)
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
    etree.dump(xml_block7)

def XML_Block_8(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2, txt_ch3, txt_ch4, txt_ch5, txt_ch6, txt_ch7, txt_ch8):
    xml_block8 = (
        E.problem(
            E.choiceresponse(
            E.label(etree.XML(txt_lbl)), 
            E.description(txt_desc),
            E.checkboxgroup(
                etree.XML(txt_ch1),
                etree.XML(txt_ch2),
                etree.XML(txt_ch3),
                etree.XML(txt_ch4),
                etree.XML(txt_ch5),
                etree.XML(txt_ch6),
                etree.XML(txt_ch7),
                etree.XML(txt_ch8)
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
    etree.dump(xml_block8)


txt_display     ='Testing'
txt_label       = '<p>How can you scale the Deployment <code>hello-world</code> from 2 to 3?</p>' 
txt_description = 'Please select all applicable options from the list below. Multiple selections are allowed.'

txt_parse1      = '<code>kubectl scale deployment hello-world --pods 3      </code>'
txt_parse2      = '<code>kubectl scale deployment hello-world --replicas 3  </code>'
txt_parse3      = '<code>kubectl scale deployment hello-world --up 1        </code>'
txt_parse4      = '<code>kubectl scale deployment hello-world 3             </code>'
txt_parse5      = '<code>kubectl scale deployment hello-world --pods 3      </code>'
txt_parse6      = '<code>kubectl scale deployment hello-world --replicas 3  </code>'
txt_parse7      = '<code>kubectl scale deployment hello-world --up 1        </code>'
txt_parse8      = '<code>kubectl scale deployment hello-world 3             </code>'

txt_choice1     = Build_Choice(txt_parse1, 'false')
txt_choice2     = Build_Choice(txt_parse2, 'true')
txt_choice3     = Build_Choice(txt_parse3, 'false')
txt_choice4     = Build_Choice(txt_parse4, 'false')
txt_choice5     = Build_Choice(txt_parse5, 'true')
txt_choice6     = Build_Choice(txt_parse6, 'false')
txt_choice7     = Build_Choice(txt_parse7, 'true')
txt_choice8     = Build_Choice(txt_parse8, 'false')


print('\n')
XML_Block_2(txt_display, txt_label, txt_description, txt_choice1, txt_choice2)
print('\n')
XML_Block_3(txt_display, txt_label, txt_description, txt_choice1, txt_choice2, txt_choice3)
print('\n')
XML_Block_4(txt_display, txt_label, txt_description, txt_choice1, txt_choice2, txt_choice3, txt_choice4)
print('\n')
XML_Block_5(txt_display, txt_label, txt_description, txt_choice1, txt_choice2, txt_choice3, txt_choice4, txt_choice5)
print('\n')
XML_Block_6(txt_display, txt_label, txt_description, txt_choice1, txt_choice2, txt_choice3, txt_choice4, txt_choice5, txt_choice6)
print('\n')
XML_Block_7(txt_display, txt_label, txt_description, txt_choice1, txt_choice2, txt_choice3, txt_choice4, txt_choice5, txt_choice6, txt_choice7)
print('\n')
XML_Block_8(txt_display, txt_label, txt_description, txt_choice1, txt_choice2, txt_choice3, txt_choice4, txt_choice5, txt_choice6, txt_choice7, txt_choice8)
print('\n')


# ----------------------------------------------------------------------------------------------------------------------------
# template example for xml_block with 4 choices ...
# ----------------------------------------------------------------------------------------------------------------------------
# def XML_Block_4(disp_name, txt_lbl, txt_desc, txt_ch1, txt_ch2, txt_ch3, txt_ch4):
#     xml_block4 = (
#         E.problem(
#             E.choiceresponse(
#             E.label(etree.XML(txt_lbl)), 
#             E.description(txt_desc),
#             E.checkboxgroup(
#                 etree.XML(txt_ch1),
#                 etree.XML(txt_ch2),
#                 etree.XML(txt_ch3),
#                 etree.XML(txt_ch4)
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
#     etree.dump(xml_block4)
# ----------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------
# OUTPUT format created by code
# ----------------------------------------------------------------------------------------------------------------------------
# <problem display_name="Testing" markdown="null" max_attempts="1" show_reset_button="false" showanswer="never" weight="1.0">
#   <choiceresponse>
#     <label>
#       <p>How can you scale the Deployment <code>hello-world</code> from 2 to 3?</p>
#     </label>
#     <description>Please select all applicable options from the list below. Multiple selections are allowed.</description>
#     <checkboxgroup>
#       <choice correct="false">
#         <code>kubectl scale deployment hello-world --pods 3      </code>
#       </choice>
#       <choice correct="true">
#         <code>kubectl scale deployment hello-world --replicas 3  </code>
#       </choice>
#       <choice correct="false">
#         <code>kubectl scale deployment hello-world --up 1        </code>
#       </choice>
#       <choice correct="false">
#         <code>kubectl scale deployment hello-world 3             </code>
#       </choice>
#     </checkboxgroup>
#   </choiceresponse>
# </problem>
# ----------------------------------------------------------------------------------------------------------------------------