import os
import re
import csv
import docx2txt
import pandas as pd
from subprocess import Popen, PIPE
from PyPDF2 import PdfReader
from striprtf.striprtf import rtf_to_text


print('Start parsing in a arenda files')
directory = '..//data//data_arenda'


def document_to_text(filename, file_path):
    if filename[-4:] == ".doc":
        cmd = ['antiword', file_path]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('UTF-8', 'ignore')


# Создание директории в которой будут храниться результаты
if not os.path.isdir("..//data//csv_s//arenda"):
    os.mkdir("..//data//csv_s//arenda")

# i = 0
big_list: list = []

for filename in os.listdir(directory):
    if filename.endswith(".doc") or \
            filename.endswith(".pdf") or \
            filename.endswith(".rtf") or \
            filename.endswith(".docx"):
        # print(os.path.join(directory, filename))
        name = os.path.join(directory, filename)

        # working with docx
        if name.endswith("docx"):
            # replace following line with location of your .docx file
            MY_TEXT = docx2txt.process(name)

            text = MY_TEXT.lower()
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

            big_list.append(unique)
            print(f'Запись результата парсига {name} в buffer прошла успешно')

        # working with doc
        elif name.endswith('doc'):
            text = document_to_text(filename=filename,
                                    file_path=name)
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

            big_list.append(unique)
            print(f'Запись результата парсига {name} в buffer прошла успешно')

        # working with pdf
        elif name.endswith('pdf'):
            reader = PdfReader(name)
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

            big_list.append(unique)
            print(f'Запись результата парсига {name} в buffer прошла успешно')

        # working with .rtf
        elif name.endswith('rtf'):
            with open(name) as infile:
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
                big_list.append(unique)
                print(f'Запись результата парсига {name} в buffer прошла успешно')
        else:
            continue

save_path = '..//data//csv_s//arenda'
completeName = os.path.join(save_path, f'data_arenda_unique' + ".txt")
csv_name = os.path.join(save_path, f'data_arenda_unique' + ".csv")

with open(completeName, 'w') as f:
    for i in range(len(big_list)):
        for j in range(len(big_list[i])):
            re.sub(r'[^\w\s]+|[\d]+', r'', str(big_list[i][j])).strip()
            re.sub(r'[0-9]', r'', str(big_list[i][j])).strip()
            f.write(str(big_list[i][j]) + '\n')
f.close()

textF: list = []
with open(completeName, 'r', encoding='utf8') as f:
    for line in f:
        textF.append(line.strip())
f.close()

"""
header = ['feature_words']
with open(csv_name, 'a+', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    writer.writerows(textF)
f.close()

read_file = pd.read_csv(completeName)
read_file.to_csv(csv_name)
"""

print('Finish parsing in a arenda files')