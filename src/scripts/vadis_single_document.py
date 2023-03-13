import subprocess

#fields document 2 : id	question_name	time_collection_max_year	title	topic	kind_data	question_type2	study_citation_en	countries_collection_en	time_collection_min_year	study_id	study_title	date	notes	kind_data_en	group_link_en	variable_name	methodology_collection_en	question_lang	methodology_collection_ddi	study_id_title	countries_collection	study_id_title_en	notes_en	topic_exploredata_orig_en	question_id	time_collection_years	methodology_collection_ddi_en	topic_exploredata_orig	group_description_en	study_lang	topic_en	variable_label_en	title_en	variable_label	study_title_en	methodology_collection	date_recency	analysis_unit


# 1.1 # '-fields', 'id', 'question_id', 'variable_label', 'question_text_en', 'study_title', 'topic_exploredata_orig_en', 'study_id', 'study_title_en', 'study_id_title_en', 'variable_label_en', 'title', 'variable_name', 'title_en', 'question_text', 'topic', 'date', 'question_label', 'question_label_en', 'time_method_en', 'study_id_title'
# 1.2 # '-fields', ['id', 'id', 'question_id', 'variable_label', 'study_title', 'topic_exploredata_orig_en', 'study_id', 'study_title_en', 'study_id_title_en', 'variable_label_en', 'title', 'variable_name', 'title_en', 'topic', 'date', 'study_id_title']
#1.3 ['id', 'id', 'question_id', 'variable_label', 'study_title', 'topic_exploredata_orig_en', 'study_id', 'study_title_en', 'study_id_title_en', 'variable_label_en', 'title', 'variable_name', 'title_en', 'topic', 'date', 'study_id_title']

# 2 # '-fields', 'variable_label', 'question_text_en', 'variable_label_en', 'title', 'title_en', 'question_text', 'topic', 'question_label', 'question_label_en'
# 2.2 # ['id', 'variable_label', 'variable_label_en', 'title', 'title_en', 'topic']

# 3 # '-fields', 'variable_label', 'question_text_en', 'variable_label_en', 'title', 'title_en', 'question_text'
# 4 # '-fields', 'study_id', 'question_label_en', 'variable_label', 'question_text_en', 'variable_label_en', 'title', 'title_en', 'question_text'



def run():

    #data_name_orig = '13391'

    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_orig+"/corpus",
    #                  data_name_orig+"_pp",
    #                  '-fields', 'analysis'])

    #data_name = '13391_fields_1'

    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_orig+"_pp/analysis_pp_targets.tsv",
    #                  data_name,
    #                  '-fields', 'id', 'question_id', 'variable_label', 'question_text_en', 'study_title',
    #                  'topic_exploredata_orig_en', 'study_id', 'study_title_en', 'study_id_title_en',
    #                  'variable_label_en', 'title', 'variable_name', 'title_en', 'question_text', 'topic', 'date',
    #                  'question_label', 'question_label_en', 'time_method_en', 'study_id_title'
    #                  ])

    # data_name = '13391_fields_2'
    #
    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_orig+"_pp/analysis_pp_targets.tsv",
    #                  data_name,
    #                  '-fields', 'variable_label', 'question_text_en', 'variable_label_en', 'title', 'title_en',
    #                  'question_text', 'topic', 'question_label', 'question_label_en'
    #                  ])

    # data_name = '13391_fields_3'
    #
    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_orig+"_pp/analysis_pp_targets.tsv",
    #                  data_name,
    #                  '-fields', 'variable_label', 'question_text_en', 'variable_label_en', 'title', 'title_en', 'question_text'
    #                ])

    #data_name = '13391_fields_4'

    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_orig+"_pp/analysis_pp_targets.tsv",
    #                  data_name,
    #                  '-fields', 'variable_label'
    #                 ])

    #data_name_orig = '11235'
    # data_name = '11235_fields_6'
    #
    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_orig+"_pp/analysis_pp_targets.tsv",
    #                  data_name,
    #                  '-fields', 'variable_label', 'variable_label_en'
    #                 ])




    #data_name = data_name_orig+"_pp"

    #data_name_lex_and_string = '13391_fields_4_lex_and_string'

    # data_name_queries = '11235_pp'
    # data_name_targets = '11235_fields_6'
    # data_name = '11235_pp_fields_6_no_retrieval_only_semantic'

    # data_name_orig = '11658'
    # data_name_queries = '11658_pp'
    # data_name = '11658_pp_queries'
    # #
    # #
    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_queries.py",
    #                  data_name_queries,
    #                  data_name_orig,
    #                  data_name
    #                 ])

    # subprocess.call(["python",
    #                  "../../src/re_ranking/re_ranking.py",
    #                  "../../data/"+data_name_queries+"/queries.tsv",
    #                  "../../data/"+data_name_targets+"/targets_labels.tsv",
    #                  data_name,
    #                  "braycurtis",
    #                  "10",
    #                  '--ranking_only',
    #                  '-sentence_embedding_models', "sentence-transformers/sentence-t5-base", "all-mpnet-base-v2",#, "https://tfhub.dev/google/universal-sentence-encoder/4"])
    #                  #'-referential_similarity_measures', "synonym_similarity", "ne_similarity",
    #                  '-lexical_similarity_measures', "similar_words_ratio", "similar_words_ratio_length",
    #                  #'-string_similarity_measures', "sequence_matching", "levenshtein"
    #                  ])
    #
    # data_name_queries = '11235_pp'
    # data_name_targets = '11235_fields_6'
    # data_name = '11235_pp_fields_6_no_retrieval'

    # data_name_targets = '13391_fields_4'
    # data_name_queries = '13391_pp_queries'
    # data_name = '13391_pp_queries_fields_4_no_retrieval'

    # data_name_queries = '11658_pp_queries'
    # data_name_targets = '11658_fields_3'
    # data_name = '11658_pp_queries_fields_3_no_retrieval_all_features'



    # data_name_orig = '20760_pp'
    #
    # data_name_targets = '20760_fields_2'
    #
    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_orig+"/corpus",
    #                  data_name_targets,
    #                  '-fields', 'variable_label', 'variable_label_en'])

    # data_name_queries = '11155'
    # data_name_targets = 'gesis_unsup'
    # data_name = '11155'

    # subprocess.call(["python",
    #                  "../../src/re_ranking/re_ranking.py",
    #                  "../../data/"+data_name_queries+"/queries.tsv",
    #                  "../../data/"+data_name_targets+"/targets_labels.tsv",
    #                  data_name,
    #                  "braycurtis",
    #                  "20",
    #                  '--ranking_only',
    #                  '-sentence_embedding_models', "sentence-transformers/sentence-t5-base", #"johngiorgi/declutr-sci-base",#, "https://tfhub.dev/google/universal-sentence-encoder/4"])
    #                  '-referential_similarity_measures', "ne_similarity",
    #                  '-lexical_similarity_measures', "similar_words_ratio"
    #                  '-string_similarity_measures', "sequence_matching", "levenshtein"
    #                  ])

    # data_name_queries = '13391_pp_queries'
    # data_name_targets = '13391_fields_4'
    # data_name = '13391_pp_queries_fields_4_no_retrieval'

    data_name_queries = '11155_pp'
    data_name_targets = 'gesis_unsup'
    new_data_name_targets = 'gesis_unsup_labels'
    data_name = '11155'

    # subprocess.call(["python",
    #                  "../../src/pre_processing/pre_processing_targets.py",
    #                  "../../data/"+data_name_targets+"/corpus",
    #                  new_data_name_targets,
    #                  '-fields', 'variable_label', 'variable_label_en'])

    data_name_targets = new_data_name_targets


    subprocess.call(["python",
                     "../../src/candidate_retrieval/retrieval.py",
                     "../../data/"+data_name_queries+"/queries.tsv",
                     "../../data/"+data_name_targets+"/corpus",
                     data_name,
                     "braycurtis",
                     "10",
                     "--union_of_top_k_per_feature",
                     '-sentence_embedding_models', "sentence-transformers/sentence-t5-base", "all-mpnet-base-v2", "princeton-nlp/sup-simcse-roberta-large",
                     '-referential_similarity_measures', "synonym_similarity", "ne_similarity",
                     '-lexical_similarity_measures', "similar_words_ratio", "similar_words_ratio_length",
                     '-string_similarity_measures', "sequence_matching", "levenshtein"])


    subprocess.call(["python",
                     "../../src/re_ranking/re_ranking.py",
                     "../../data/"+data_name_queries+"/queries.tsv",
                     "../../data/"+data_name_targets+"/corpus",
                     data_name,
                     "braycurtis",
                     "10",
                     '-sentence_embedding_models', "sentence-transformers/sentence-t5-base", "all-mpnet-base-v2", "princeton-nlp/sup-simcse-roberta-large",#, "https://tfhub.dev/google/universal-sentence-encoder/4"])
                     #'-referential_similarity_measures', "synonym_similarity", "ne_similarity",
                     #'-lexical_similarity_measures', "similar_words_ratio", "similar_words_ratio_length",
                     #'-string_similarity_measures', "sequence_matching", "levenshtein"
                     ])


if __name__ == "__main__":
    run()