from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (update this with your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\RanaUniverse\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

image = Image.open("4.jpg")

# Perform OCR and print the result
text = pytesseract.image_to_string(image)
print("Extracted Text:\n", text)
print(len(text))

output_file_path = "aaa.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(text)

# Notify the user
print(f"Text has been saved. 🍌🍌🍌")