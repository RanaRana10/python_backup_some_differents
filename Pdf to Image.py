# This will Make all page of pdf to different images in a Folder By Rana Universe
import fitz  # PyMuPDF, PIP PyMuPDF [https:t.me/RanaUniverse]
import os

# Specify the PDF file path
pdf_file = r'C:\Users\RanaUniverse\Desktop\RanaUniverse.pdf'

# Specify the output directory
output_directory = 'Rana Universe PDF Images'

# Output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

pdf_document = fitz.open(pdf_file)

for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]
    image = page.get_pixmap()
    image_file = os.path.join(output_directory, f'page_{page_number}.png')
    image.save(image_file, 'png')

pdf_document.close()
