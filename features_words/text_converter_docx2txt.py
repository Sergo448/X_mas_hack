import docx2txt

# replace following line with location of your .docx file
MY_TEXT = docx2txt.process("2d4708c800dc003466fa9a8a64e2e2b7.docx")


with open("Output.txt", "w") as text_file:
    print(MY_TEXT, file=text_file)