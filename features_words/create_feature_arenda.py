import os
import docx2txt

from docx import Document

directory = '..//data//data_arenda'

# Создание директории в которой будут храниться результаты
if not os.path.isdir("..//data//csv_s//arenda"):
    os.mkdir("..//data//csv_s//arenda")

i = 0

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
        if name.endswith('doc')


        save_path = '..//data//csv_s//arenda'
        completeName = os.path.join(save_path, f'data_arenda_unique_{i}' + ".csv")
        with open(completeName, 'w') as f:
            f.write(str(unique) + '\n')
        i += 1

    else:
        continue
