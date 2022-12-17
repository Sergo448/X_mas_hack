import json
import shutil
import os
from os import path
import pandas as pd

"""
Получает на вход путь к файлу .json и к директории с документами и 
составляет один объект датафрейма для последующей работы.
"""


def make_data_3(path_json: str, source_path: str):
    if type(path_json) != str or type(source_path) != str:
        raise ValueError('Have error in paths types')
    else:
        f = open(path_json)
        data_json_1 = json.load(f)

        get_files = os.listdir(source_path)
        buf_1: list = []
        buf_2: list = []

        keys_l: list = []
        values_l: list = []

        for g in get_files:
            buf_1.append(source_path + '//' + g)
            buf_2.append(g)

        for keys, values in data_json_1.items():
            keys_l.append(keys)
            values_l.append(values)

        data_for_merge_1 = pd.DataFrame(data={'doc': buf_2,
                                              'path': buf_1})
        data_for_merge_2 = pd.DataFrame(data={'doc': keys_l,
                                              'type': values_l})
        data = data_for_merge_1.merge(data_for_merge_2, on='doc')

        return data


# create all paths to directories
path_to_data_arenda: str = ".//data_for_test//data_arenda"
path_to_data_kupi_prodai: str = ".//data_for_test//data_kupi_prodai"
path_to_data_podriad: str = ".//data_for_test//data_podriad"
path_to_data_postavka: str = ".//data_for_test//data_postavka"
path_to_data_uslugi: str = ".//data_for_test//data_uslugi"

# sourse path
source_path = ".//data_for_test//hacka-aka-embedika//docs"
path_to_json = './/data//DataFiles//hacka-aka-embedika//classes.json'

data = make_data_3(path_json=path_to_json, source_path=source_path)
data_list = data.values.tolist()

for i in range(len(data_list)):
    if 'Договоры для акселератора/Договоры аренды' in data_list[i][2]:
        new_location_d_arenda = shutil.move(source_path, path_to_data_arenda)
        print("% s перемещен в указанное место,% s" % (data_list[i][1], new_location_d_arenda))

    elif 'Договоры для акселератора/Договоры купли-продажи' in data_list[i][2]:
        new_location_d_arenda = shutil.move(source_path, path_to_data_arenda)
        print("% s перемещен в указанное место,% s" % (data_list[i][1], new_location_d_arenda))

    elif 'Договоры для акселератора/Договоры подряда' in data_list[i][2]:
        new_location_d_arenda = shutil.move(source_path, path_to_data_arenda)
        print("% s перемещен в указанное место,% s" % (data_list[i][1], new_location_d_arenda))

    elif 'Договоры для акселератора/Договоры поставки' in data_list[i][2]:
        new_location_d_arenda = shutil.move(source_path, path_to_data_arenda)
        print("% s перемещен в указанное место,% s" % (data_list[i][1], new_location_d_arenda))

    elif 'Договоры для акселератора/Договоры оказания услуг' in data_list[i][2]:
        new_location_d_arenda = shutil.move(source_path, path_to_data_arenda)
        print("% s перемещен в указанное место,% s" % (data_list[i][1], new_location_d_arenda))
