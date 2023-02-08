import json
import pickle
from pathlib import Path

import pandas as pd

from src.get_data import DATA_PATH
from src.utils import load_pickled_object


def get_variable_dataset(corpus_id):
    example_file_path = DATA_PATH + "gesis_unsup/vocab/vocab/"+str(corpus_id)+".pkl"
    return pickle.load(open(example_file_path, 'rb'))


def tokenize_document(full_text):
    text_chunks = []
    return text_chunks


def create_queries_and_targets_for_document(document_n):

    queries_df =  pd.DataFrame(columns=['uuid', 'text'])
    with open(DATA_PATH + "gesis_unsup/vadis_pubs_corpus.json") as f:
        documents_dict = json.load(f)
    document = list(documents_dict.items())[document_n]
    document_id = document[0]
    document_content = document[1]

    Path(DATA_PATH + document_id).mkdir(parents=True, exist_ok=True)
    queries_data_path = DATA_PATH + document_id + "/queries.tsv"
    targets_data_path = DATA_PATH + document_id + "/corpus"

    #document_fulltext = document_content["fulltext"]
    document_sentences = document_content["sentence_tokens"]
    queries_df['text'] = pd.Series(document_sentences)
    queries_df['uuid'] = queries_df.index

    queries_df.to_csv(queries_data_path, sep='\t', header=False, index=False)

    related_datsets = document_content["related_research_datasets"]

    for ds in related_datsets:
        variables = get_variable_dataset(ds)
        all_variable_parts = []
        variable_fields_info = {}
        for variable in variables.items():
            variable_fields = variable[1]['_source']
            for field in variable_fields.keys():
                variable_fields_info[field] = 0
        for variable in variables.items():
            variable_fields = variable[1]['_source']
            for field in variable_fields.keys():
                variable_fields_info[field] += 1
            all_variable_parts.extend(list(variable_fields.keys()))
    print(variable_fields_info)
    all_variable_parts = list(set(all_variable_parts))
    columns = ['id'] + all_variable_parts
    corpus_df = pd.DataFrame(columns=columns)
    for ds in related_datsets:
        variables = get_variable_dataset(ds)
        for variable in variables.items():
            this_row = []
            id = variable[0]
            this_row = this_row + [id]
            variable_fields = variable[1]['_source']
            for column in columns[1:]:
                if column in variable_fields.keys():
                    this_row = this_row + [variable_fields[column]]
                else:
                    this_row = this_row + [" "]
            target_df = pd.DataFrame([this_row], columns=columns)
            corpus_df = pd.concat([corpus_df, target_df], names=columns)
    corpus_df.to_csv(targets_data_path, sep='\t', header=True, index=False)

create_queries_and_targets_for_document(3)






