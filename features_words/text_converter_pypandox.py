import pypandoc

# Example file:
docxFilename = '2d4708c800dc003466fa9a8a64e2e2b7.docx'
output = pypandoc.convert_file(docxFilename, 'plain', outputfile="somefile.txt")
assert output == ""
