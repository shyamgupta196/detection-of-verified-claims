import subprocess


def run():

    data_name = 'clef_2022_checkthat_2a_english'

    # subprocess.call(["python",
    #                  "../../src/candidate_retrieval/retrieval.py",
    #                  "../../data/"+data_name+"/queries.tsv",
    #                  "../../data/"+data_name+"/corpus",
    #                  data_name,
    #                  "braycurtis",
    #                  "10",
    #                  "--union_of_top_k_per_feature",
    #                  '-sentence_embedding_models', "sentence-transformers/sentence-t5-base", "all-mpnet-base-v2", "princeton-nlp/sup-simcse-roberta-large",
    #                  '-referential_similarity_measures', "synonym_similarity", "ne_similarity",
    #                  '-lexical_similarity_measures', "similar_words_ratio", "similar_words_ratio_length",
    #                  '-string_similarity_measures', "sequence_matching", "levenshtein"])
    #
    # subprocess.call(["python", "../../evaluation/scorer/recall_evaluator.py",
    #                  data_name,
    #                  "../../data/"+data_name+"/gold.tsv"])

    subprocess.call(["python",
                     "../../src/re_ranking/re_ranking.py",
                     "../../data/"+data_name+"/queries.tsv",
                     "../../data/"+data_name+"/corpus",
                     data_name,
                     "braycurtis",
                     "10",
                     '--supervised',
                     '-sentence_embedding_models', "sentence-transformers/sentence-t5-base", "all-mpnet-base-v2",#, "https://tfhub.dev/google/universal-sentence-encoder/4"])
                     #'-referential_similarity_measures', "synonym_similarity", "ne_similarity",
                     '-lexical_similarity_measures', "similar_words_ratio", "similar_words_ratio_length",
                     #'-string_similarity_measures', "sequence_matching", "levenshtein"
                     ])

    subprocess.call(["python", "../../evaluation/scorer/main.py",
                     "../../data/"+data_name+"/gold.tsv",
                     "../../data/" + data_name + "/pred_qrels_supervised.tsv"])
                     #"../../data/"+data_name+"/pred_qrels.tsv"])
    


    







if __name__ == "__main__":
    run()