# Import the module
from docx import *

# Open the .docx file
document = opendocx(r"C:\Users\anusha.raparthi\Desktop\Division wise Type of Changes\Type of Change_AVET(USA).docx")
print(document)
# Search returns true if found
#search(document,'your sea')