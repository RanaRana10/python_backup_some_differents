# Merge PDF to one PDF By RanaUniverse (https://t.me/RanaUniverse 🍌🍌🍌)

import PyPDF2
import os

#Input directory of PDF files to merge
input_directory = r'C:\Users\RanaUniverse\Desktop\Rana Universe'  # Replace with the path to your PDF files

#output Directory
output_directory = r'C:\Users\RanaUniverse\Desktop'  # Your output folder
output_pdf = os.path.join(output_directory, 'Rana Universe Merge PDF.pdf')
# output_pdf = 'merged3.pdf' #If you want to make in same directory disable previous 2 lines



# PDF merger object
pdf_merger = PyPDF2.PdfMerger()

# List all PDF files
pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]



# pdf_files.sort() #This line for only alphabetical shorts
pdf_files.sort(key=lambda x: int(x.split('.')[0]))  # Sort by the numeric part of the filename


total_files = len(pdf_files)


# Merging Code
for i, pdf_file in enumerate(pdf_files, 1):
    pdf_path = os.path.join(input_directory, pdf_file)
    pdf_merger.append(pdf_path)
    
    # Calculate and display progress as a percentage
    progress = (i / total_files) * 100
    print(f'Progress: {progress:.2f}%', end='\r')  # \r moves the cursor to the beginning of the line

# Write the merged PDF to the output file
with open(output_pdf, 'wb') as output_file:
    pdf_merger.write(output_file)

pdf_merger.close()

print(f'Merged PDF saved as {output_pdf} By Rana Universe 🍌🍌🍌')
