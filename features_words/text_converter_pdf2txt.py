from PyPDF2 import PdfReader

reader = PdfReader("4a5707e447271a188a1211606b158a94.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]
# finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
        # sort
        unique.sort()

print(unique)