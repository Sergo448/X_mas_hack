import aspose.words as aw
import aspose


doc = aspose.words.Document("0ca2f9faecdbc67d6686a9f5b6636eba.doc")
text = doc.save("Outputtt.txt")

print(text)

# Create and save a simple document
doc = aw.Document('0ca2f9faecdbc67d6686a9f5b6636eba.doc')
builder = aw.DocumentBuilder(doc)
builder.writeln("Hello Aspose.Words for Python via .NET")

doc.save("out.docx")