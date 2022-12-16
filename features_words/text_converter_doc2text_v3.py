from subprocess import Popen, PIPE


def document_to_text(filename, file_path):
    if filename[-4:] == ".doc":
        cmd = ['antiword', file_path]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')


text = document_to_text(filename='0ca2f9faecdbc67d6686a9f5b6636eba.doc',
                        file_path='//home//sergey//PycharmProjects//X_mas_hack//features_words'
                                  '//0ca2f9faecdbc67d6686a9f5b6636eba.doc')
