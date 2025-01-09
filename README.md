
# SimBa

This method enables fact-checking of arbitrary claims or statements (e.g. taken from online discourse and social media posts). It takes advantage of a unique and constantly updated repository of fact-checked claims mined from the web (ClaimsKG).

ClaimsKG is a structured KnowledgeBase which serves as a registry of claims. The KB is updated at regular intervals. Thea latest release of ClaimsKG contains 74000 claims collected from 13 different fact-checking websites from the year 1996 to 2023. For more details regarding ClaimsKG like the latest release and related papers, please refer to the official webpage https://data.gesis.org/claimskg/

The method receives an input claim/sentence , computes similarity with 74000 previously fact-checked claims from ClaimsKG and returns a set of ranked claims from , their relevance scores, veracity ratings and the corresponding fact-check sources

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

      

### 4. Run the Project
Once everything is installed, you can run the SimBa project. To do so, use the following command in the terminal:

      python check_that.py

## Keywords
verified claims retrieval, semantic similarity, claims ranking

## Social Science Usecase
  1. A social scientist focuses on misinformation in the social media discourse during political events and wants to verify the veracity of a fact-checked claim .
  2. A social scientist wants to find out if a claim/statement has been fact-checked before.
  3. A social scientist wants to find similar statements/claims that have been previously fact-checked      

## Repository Structure

## Results

| Datast  | Map@1 | Map@3     | Map@5 |  
|---|---|-----------|---|
| 2020 2a English  | 0.9425  |  0.9617   |  0.9617
| 2021 2a English  | 0.9208  | 0.9431    |  0.9450     
| 2021 2b English  | 0.4114  | 0.4388    |  0.4414 
| 2022 2a English  | 0.9043  | 0.9258    |  0.9258 
| 2022 2b English  | 0.4462  | 0.4744    |  0.4805


## Arcitecture

1. Retrieval
2. Re-Ranking
3. Learning


## Contact
For further assistance or inquiries, please contact: ali.elboukili@gesis.org






