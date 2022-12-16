import json
import shutil
import os
from os import path

# Opening JSON file
f = open('.//data//DataFiles//hacka-aka-embedika//classes.json')

# returns JSON object as
# a dictionary
data_json = json.load(f)

# create all paths to directories
path_to_data_arenda = ".//data//data_arenda"
path_to_data_kupi_prodai = ".//data//data_kupi_prodai"
path_to_data_podriad = ".//data//data_podriad"
path_to_data_postavka = ".//data//data_postavka"
path_to_data_uslugi = ".//data//data_uslugi"

# sourse path
source_path = ".//data//DataFiles//hacka-aka-embedika//docs"

# Iterating through the json
# list
for keys, values in data_json.items():
    print(keys, values)
    if path.exists(source_path):
        if 'Договоры для акселератора/Договоры аренды' in values:
            new_location_d_arenda = shutil.move(source_path, path_to_data_arenda)
            print("% s перемещен в указанное место,% s" % (source_path, new_location_d_arenda))

        elif 'Договоры для акселератора/Договоры купли-продажи' in values:
            new_location_d_kupi_prodai = shutil.move(source_path, path_to_data_kupi_prodai)
            print("% s перемещен в указанное место,% s" % (source_path, new_location_d_kupi_prodai))

        elif 'Договоры для акселератора/Договоры подряда' in values:
            new_location_d_podriad = shutil.move(source_path, path_to_data_podriad)
            print("% s перемещен в указанное место,% s" % (source_path, new_location_d_podriad))

        elif 'Договоры для акселератора/Договоры поставки' in values:
            new_location_d_postavka = shutil.move(source_path, path_to_data_postavka)
            print("% s перемещен в указанное место,% s" % (source_path, new_location_d_postavka))

        elif 'Договоры для акселератора/Договоры оказания услуг' in values:
            new_location_d_uslugi = shutil.move(source_path, path_to_data_uslugi)
            print("% s перемещен в указанное место,% s" % (source_path, new_location_d_uslugi))

        else:
            print('Correct files are not exists in the source directory')
    else:
        print('File is not exist')
# Closing file
f.close()









