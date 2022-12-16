import doc2text

# Initialize the class.
doc = doc2text.Document()


doc.read('2d4708c800dc003466fa9a8a64e2e2b7.docx')

# Crop the pages down to estimated text regions, deskew, and optimize for OCR.
doc.process()

# Extract text from the pages.
doc.extract_text()
text = doc.get_text()

with open("Output.txt", "w") as text_file:
    print(text, file=text_file)