import os
import shutil
import subprocess
from pathlib import Path


def run():
    # Fixed dataset name
    data_name = "clef2022"

    # Input query file for SimBa as independent repo
    data_name_queries = "data/" + data_name + "/queries.tsv"

    # Verified candidate claims file for SimBa as independent repo
    data_name_targets = "data/" + data_name + "/corpus.tsv"

    # Path to this script's directory
    directory_path = os.path.dirname(__file__)

    # Run candidate retrieval
    subprocess.call([
        "python",
        os.path.join(directory_path, "src/candidate_retrieval/retrieval.py"),
        data_name_queries,
        data_name_targets,
        data_name,
        data_name,
        "braycurtis",
        "50",
        "-sentence_embedding_models", "all-mpnet-base-v2"
    ])

    # Run re-ranking
    subprocess.call([
        "python",
        os.path.join(directory_path, "src/re_ranking/re_ranking.py"),
        data_name_queries,
        data_name_targets,
        data_name,
        data_name,
        "braycurtis",
        "5",
        "-sentence_embedding_models", 
        "all-mpnet-base-v2", 
        "sentence-transformers/sentence-t5-base", 
        "princeton-nlp/unsup-simcse-roberta-base",
        "-lexical_similarity_measures", "similar_words_ratio"
    ])

    # Gold qrel labels file for SimBa as independent repo
    data_name_gold = "data/" + data_name + "/gold.tsv"

    # Evaluation
    """
    Uncomment this block to evaluate the results if you have the evaluation script ready.
    
    print("Evaluation Scores for dataset " + data_name)
    subprocess.call([
        "python", os.path.join(directory_path, "evaluation/scorer/main.py"),
        data_name_gold,
        "data/" + data_name + "/pred_qrels.tsv"
    ])
    """

    # Ensure output directory exists
    Path("run0").mkdir(parents=True, exist_ok=True)

    # Copy the prediction file to the output directory
    output_file = "data/" + data_name + "/pred_qrels.tsv"
    new_file = "run0/" + data_name + ".tsv"

    shutil.copy(output_file, new_file)


if __name__ == "__main__":
    run()
