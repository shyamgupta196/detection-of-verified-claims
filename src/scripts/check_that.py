import shutil
import subprocess
from pathlib import Path


def run():

    data_names = ['clef_2020_checkthat_2_english', 'clef_2021_checkthat_2a_english', 'clef_2021_checkthat_2b_english', 'clef_2022_checkthat_2a_english', 'clef_2022_checkthat_2b_english']

    for data_name in data_names:

        # data_name_queries =
        # data_name_targets = "../../2021-2a-vclaims.tsv"
        # data_name_targets = "../../2021-2a-vclaims.tsv"
        # data_name_targets = "../../2021-2b-vclaims.tsv"
        # data_name_targets = "../../2022-2a-vclaims.tsv"
        # data_name_targets = "../../2022-2b-vclaims.tsv"

        # gold_qrels = {"2020a": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2020-factchecking-task2/test-input/tweet-vclaim-pairs.qrels"),
        #               "2021a": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2021-checkthat-lab/task2/test-gold/subtask-2a--english/qrels-test.tsv"),
        #               "2021b": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2021-checkthat-lab/task2/test-gold/subtask-2b--english/task2b-test.tsv"),
        #               "2022a": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2022-checkthat-lab/task2/data/subtask-2a--english/test/CT2022-Task2A-EN-Test_Qrels_gold.tsv"),
        #               "2022b": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2022-checkthat-lab/task2/data/subtask-2b--english/test/CT2022-Task2B-EN-Test_Qrels_gold.tsv")}

        # gold_qrels = {"2020a": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2020-factchecking-task2/test-input/tweets.queries.tsv"),
        #               "2021a": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2021-checkthat-lab/task2/test-gold/subtask-2a--english/tweets.queries.tsv"),
        #               "2021b": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2021-checkthat-lab/task2/test-gold/subtask-2b--english/queries.tsv"),
        #               "2022a": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2022-checkthat-lab/task2/data/subtask-2a--english/test/CT2022-Task2A-EN-Test_Queries_gold.tsv"),
        #               "2022b": os.path.join(base_path,
        #                                     "claimlinking_riet/claimlinking_clef2022-checkthat-lab/task2/data/subtask-2b--english/test/CT2022-Task2B-EN-Test_Queries_gold.tsv")}


        subprocess.call(["python",
                         "../../src/candidate_retrieval/retrieval.py",
                         "../../data/"+data_name+"/queries.tsv",
                         "../../data/"+data_name+"/corpus",
                         data_name,
                         data_name,
                         "braycurtis",
                         "50",
                         '-sentence_embedding_models', "all-mpnet-base-v2"
                         ])

        subprocess.call(["python", "../../evaluation/scorer/recall_evaluator.py",
                         data_name,
                         "../../data/"+data_name+"/gold.tsv"])

        subprocess.call(["python",
                         "../../src/re_ranking/re_ranking.py",
                         "../../data/"+data_name+"/queries.tsv",
                         "../../data/"+data_name+"/corpus",
                         data_name,
                         data_name,
                         "braycurtis",
                         "5",
                         '-sentence_embedding_models', "all-mpnet-base-v2", "sentence-transformers/sentence-t5-base", "princeton-nlp/unsup-simcse-roberta-base",
                         '-lexical_similarity_measures', "similar_words_ratio"
                         ])

        print("Evaluation Scores for dataset "+ data_name)
        subprocess.call(["python", "../../evaluation/scorer/main.py",
                         "../../data/"+data_name+"/gold.tsv",
                         "../../data/" + data_name + "/pred_qrels.tsv"]),

        Path("../../run0").mkdir(parents=True, exist_ok=True)

        output_file = "../../data/" + data_name + "/pred_qrels.tsv"
        if data_name == "clef_2020_checkthat_2_english":
            new_file = "../../run0/2020.tsv"
        if data_name == "clef_2021_checkthat_2a_english":
            new_file = "../../run0/2021a.tsv"
        if data_name == "clef_2021_checkthat_2b_english":
            new_file = "../../run0/2021b.tsv"
        if data_name == "clef_2022_checkthat_2a_english":
            new_file = "../../run0/2022a.tsv"
        if data_name == "clef_2022_checkthat_2b_english":
            new_file = "../../run0/2022b.tsv"

        shutil.copy(output_file, new_file)


if __name__ == "__main__":
    run()