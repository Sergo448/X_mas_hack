from striprtf.striprtf import rtf_to_text
import re

with open("4db6b233fda895c3bffcb5fdc5b8e1de.rtf") as infile:
    content = infile.read()
    text = rtf_to_text(content)

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

for i in range(len(unique)):
    re.sub(r'[^\w\s]+|[\d]+', r'', unique[i]).strip()

for i in range(len(unique)):
    re.sub(r'[0-9]', r'', unique[i])


print(unique)