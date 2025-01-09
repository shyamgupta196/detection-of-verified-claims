
# SimBa

This method facilitates fact-checking of arbitrary claims or statements (e.g. taken from online discourse and social media posts). It takes advantage of a unique and constantly updated repository of fact-checked claims mined from the web (ClaimsKG).

ClaimsKG is a structured knowledge base (KB) which serves as a registry of claims. The KB is updated at regular intervals. The latest release of ClaimsKG contains 74000 claims collected from 13 different fact-checking websites from the year 1996 to 2023. For more details regarding ClaimsKG, please refer to the official webpage https://data.gesis.org/claimskg/

The method receives an input claim/sentence, computes similarity with 74000 previously fact-checked claims from ClaimsKG and returns a set of ranked claims, their relevance scores, veracity ratings and the corresponding fact-check sources. 

## Keywords
verified claim retrieval, semantic similarity, detection of previously fact-checked claims

## Social Science Usecase
  1. Check the veracity of claims uttered online to analyze misinformation spread
  2. Find out which claims have been fact-checked before and which have not to gain information on perceived check-worthiness of statements
  3. Find claims that are semantically similar to claims that have been previously fact-checked to analyze information spread


# SimBa Project Installation and Setup Guide

This version of SimBa has been tested with **Python 3.11.6** on Windows. Using other Python versions and/or operating systems might require other package versions. 

Follow the steps below to install SimBa on your system using the recommended setup. 

## 1. **Install Python (Version 3.11.6)**

1. **Download Python 3.11.6** from the official Python website:  
   [https://www.python.org/downloads/release/python-3116/](https://www.python.org/downloads/release/python-3116/).

2. **Install Python**:
   - **During installation**, make sure to **check the box** that says **"Add Python to PATH"**. This step is crucial, as it ensures that Python and pip (Python's package manager) are available in your terminal or command prompt.
   - Follow the on-screen instructions to complete the installation.

3. **Verify the Installation**:
   After installation, open your terminal (or command prompt) and type the following command to check if Python was installed correctly:
   ```bash
   python --version


### 2. **Clone the Repository and Navigate to the Main Project Directory**
 To download SimBa, clone the repository from GitHub.

 Run the following commands in your terminal or command prompt: 
       
       git clone <repository-url>

       cd <repository name>
    

### 3. **Install Required Dependencies and Data**
 SimBa's required libraries and dependencies are listed in the requirements.txt file. Install them using the following command:
      
      pip install -r requirements.txt

To download data required by the NLTK library, start the Python interpreter
```
    python
```

then use nltk's download method:

```
    import nltk
    nltk.download(‘stopwords’)
    nltk.download(‘punkt’)
```
Afterwards, exit the interpreter:
```
    exit()
```


# How to Use
Once everything is installed, you can run the SimBa project. To do so, use the following command in the terminal:

      python main.py


## Repository Structure
...

## Input Data

### Required
The required input consists of an input query file ("queries.tsv"): 
a text file in .tsv format (tab-separated) containing one claim per line. For each of the claims, SimBA will retrieve the most similar fact-checked claims in ClaimsKG. 

### Optional
If desired, different corpus than ClaimsKG can be supplied as database ("corpus.tsv"). 

If available, a goldstandard can be supplied which lists the optimal results ("gold.tsv"). This can be used to evaluate SimBA's performance. 

## Sample Input
...

## Output Data
...

## Sample Output
...

## Architecture

SimBA is fully unsupervised, i.e. it does not need any training data. 
It operates in two steps:

1. Candidate Retrieval
2. Re-Ranking

In the first step, the semantically most similar claims are retrieved as candidates. Semantic similarity is computed using sentence embeddings. 
In a second step, a computationally more costly re-ranking step is applied to all candidates in order to find the best matches. Again, sentence embeddings combined with a lexical feature are used. 

SimBA was evaluated on the CLEF CheckThat! Lab ClaimLinking challenge data and achieved the following scores: 

| Datast  | Map@1 | Map@3     | Map@5 |  
|---|---|-----------|---|
| 2020 2a English  | 0.9425  |  0.9617   |  0.9617
| 2021 2a English  | 0.9208  | 0.9431    |  0.9450     
| 2021 2b English  | 0.4114  | 0.4388    |  0.4414 
| 2022 2a English  | 0.9043  | 0.9258    |  0.9258 
| 2022 2b English  | 0.4462  | 0.4744    |  0.4805

For more details about this method, please refer to the following publications: 

Hövelmeyer, Alica, Katarina Boland, and Stefan Dietze. 2022. "SimBa at CheckThat! 2022: Lexical and Semantic Similarity-Based Detection of Verified Claims in an Unsupervised and Supervised Way." In CLEF Working Notes 2022, Proceedings of the Working Notes of CLEF 2022- Conference and Labs of the Evaluation Forum, edited by Guglielmo Faggioli, Nicola Ferro, Allan Hanbury, and Martin Potthast, CEUR Workshop Proceedings 3180, 511-531. Aachen: RWTH Aachen. https://ceur-ws.org/Vol-3180/paper-40.pdf. 

Boland, Katarina, Hövelmeyer, Alica, Fafalios, Pavlos, Todorov, Konstantin, Mazhar, Usama, & Dietze, Stefan (2023). Robust and efficient claim retrieval for online fact-checking applications. Pre-print. https://doi.org/10.21203/rs.3.rs-3007151/v1


## Contact
For further assistance or inquiries, please contact: katarina.boland@hhu.de






