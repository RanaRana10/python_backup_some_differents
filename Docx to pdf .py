from docx2pdf import convert #pip install docx2pdf & i need to install the ms software installed already

# Replace 'aaa.docx' with the path to your DOCX file
input_docx = 'aaa.docx'

# Convert 'aaa.docx' to PDF in the same folder
convert(input_docx)

print(f'Conversion complete. PDF file saved as {input_docx.replace(".docx", ".pdf")}')


""" This part is for multiple docx in one folder"""


from docx2pdf import convert
import os

# Replace 'input_folder' with the path to your folder containing DOCX files
input_folder = 'input_folder'

# Batch convert all DOCX files in the folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".docx"):
        file_path = os.path.join(input_folder, file_name)
        convert(file_path)

print('Batch conversion complete.')
