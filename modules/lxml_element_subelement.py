from lxml import etree

DISPLAY_NAME = "Testing"
MARKDOWN     = "null"
MAX_ATTEMPTS = "1"
SHOW_RES_BTN = "false"
SHOWANSWER   = "never"
WEIGHT       = "1.0"

problem = etree.Element("problem")
problem.set ("display_name", DISPLAY_NAME)
problem.set ("markdown", MARKDOWN)
problem.set ("max_attempts", MAX_ATTEMPTS)
problem.set ("show_reset_button", SHOW_RES_BTN)
problem.set ("showanswer", SHOWANSWER)
problem.set ("weight", WEIGHT)


choiceresponse = etree.SubElement(problem, "choiceresponse")

label = etree.SubElement(choiceresponse, "label")
para = etree.SubElement(label, "p")

para.XML("How can you scale the Deployment <code>hello-world</code> from 2 to 3?")

descritpion = etree.SubElement(choiceresponse, "description")
descritpion.text = "Please select all applicable options from the list below. Multiple selections are allowed."

checkboxgroup = etree.SubElement(choiceresponse, "checkboxgroup")

choice = etree.SubElement(checkboxgroup, "choice")
choice.text = "Store images and documents from web applications."
choice.set ("correct", "true")

choice = etree.SubElement(checkboxgroup, "choice")
choice.text = "Storing backups."
choice.set ("correct", "true")

choice = etree.SubElement(checkboxgroup, "choice")
choice.text = "Hosting a WordPress website without Exoscale Compute."
choice.set ("correct", "false")

choice = etree.SubElement(checkboxgroup, "choice")
choice.text = "Using it as storage under a database server."
choice.set ("correct", "false")

etree.dump(problem)

# ----------------------------------------------------------------------------------------------------------------------------
# OUTPUT from code above
# ----------------------------------------------------------------------------------------------------------------------------
# <problem display_name="Testing" markdown="null" max_attempts="1" show_reset_button="false" showanswer="never" weight="1.0">
#   <choiceresponse>
#     <label>
#       <p>How can you scale the Deployment hello-world from 2 to 3?</p>
#     </label>
#     <description>Please select all applicable options from the list below. Multiple selections are allowed.</description>
#     <checkboxgroup>
#       <choice correct="true">Store images and documents from web applications.</choice>
#       <choice correct="true">Storing backups.</choice>
#       <choice correct="false">Hosting a WordPress website without Exoscale Compute.</choice>
#       <choice correct="false">Using it as storage under a database server.</choice>
#     </checkboxgroup>
#   </choiceresponse>
# </problem>


#    <label>
#      <p>How can you scale the Deployment <code>hello-world</code> from 2 to 3?</p>
#    </label>