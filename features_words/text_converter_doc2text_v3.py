from subprocess import Popen, PIPE
import os

directory = '..//data//data_arenda'


def document_to_text(filename, file_path):
    if filename[-4:] == ".doc":
        cmd = ['antiword', file_path]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('UTF-8', 'ignore')


for filename in os.listdir(directory):
    if filename.endswith(".doc") or \
            filename.endswith(".pdf") or \
            filename.endswith(".rtf") or \
            filename.endswith(".docx"):
        # print(os.path.join(directory, filename))
        name = os.path.join(directory, filename)

        """
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
            """
        if name.endswith('doc'):
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


print(unique)
"""text = document_to_text(filename='0ca2f9faecdbc67d6686a9f5b6636eba.doc',
                        file_path='//home//sergey//PycharmProjects//X_mas_hack//features_words'
                                  '//0ca2f9faecdbc67d6686a9f5b6636eba.doc')"""

