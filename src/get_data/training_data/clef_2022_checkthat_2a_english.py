import requests
from zipfile import ZipFile
from pathlib import Path
from os.path import join
from os import listdir, rmdir
from shutil import move

from src.get_data import DATA_PATH


def run():

    data_name = "clef_2022_checkthat_2a_english"
    directory = DATA_PATH + 'training/' + data_name

    Path(directory).mkdir(parents=True, exist_ok=True)
    general_path = directory


    queries_path = general_path + "/queries.tsv"
    qrels_path = general_path + "/gold.tsv"


    queries = requests.get('https://gitlab.com/checkthat_lab/clef2022-checkthat-lab/clef2022-checkthat-lab/-/raw/main/task2/data/subtask-2a--english/CT2022-Task2A-EN-Train-Dev_Queries.tsv')
    with open(queries_path, 'wb') as f:
        f.write(queries.content)
    dev_qrels = requests.get('https://gitlab.com/checkthat_lab/clef2022-checkthat-lab/clef2022-checkthat-lab/-/raw/main/task2/data/subtask-2a--english/CT2022-Task2A-EN-Dev_QRELs.tsv')
    with open(directory+"/dev_qrels.tsv", 'wb') as f:
        f.write(dev_qrels.content)
    train_qrels = requests.get('https://gitlab.com/checkthat_lab/clef2022-checkthat-lab/clef2022-checkthat-lab/-/raw/main/task2/data/subtask-2a--english/CT2022-Task2A-EN-Train_QRELs.tsv')
    with open(directory+"/train_qrels.tsv", 'wb') as f:
        f.write(train_qrels.content)

    


if __name__ == "__main__":
    run()