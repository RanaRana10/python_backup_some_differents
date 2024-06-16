# this will see progress bar, all pdf from any directory

import fitz  # PyMuPDF
import os
import sys

# Specify the input directory containing PDF files
input_directory = 'C:/Users/RanaUniverse/Desktop/Rana Universe'

# Specify the output directory for images
output_directory = 'PDF to Images'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all PDF files in the input directory
pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]

total_pdfs = len(pdf_files)

for idx, pdf_file in enumerate(pdf_files):
    # Construct the full path to the input PDF file
    pdf_path = os.path.join(input_directory, pdf_file)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through the pages and save them as images in the output directory
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        image_file = os.path.join(output_directory, f'{pdf_file}_{page_number}.png')
        image.save(image_file, 'png')

    # Close the PDF file
    pdf_document.close()

    # Calculate and display the progress percentage
    progress = (idx + 1) / total_pdfs * 100
    sys.stdout.write(f'\rProgress: {progress:.2f}%')
    sys.stdout.flush()

print("\nConversion completed By RanaUniverse.")
