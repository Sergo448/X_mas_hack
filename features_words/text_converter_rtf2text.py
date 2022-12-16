from striprtf.striprtf import rtf_to_text
import re
import os
import tqdm
import textract
import ftfy

def get_file_list(root_folder):
    file_content = {}
    pattern = re.compile('[\W_]')
    file_list = [f for f in os.listdir(root_folder)]
    for f in tqdm(file_list):
        if "rtf" not in f:
            f_text = textract.process(os.path.join(root_folder, f))
            text = ftfy.ftfy((f_text).decode('utf-8'))
        if ".rtf" in f:
            with open(os.path.join(root_folder, f)) as infile:
                content = infile.read()
                text = rtf_to_text(content)
        file_content[f] = pattern.sub(' ', text).lower().lstrip().rstrip().replace('  ', ' ')

    return file_content
