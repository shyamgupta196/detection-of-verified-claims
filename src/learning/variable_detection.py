import pandas as pd

from sklearn import naive_bayes, preprocessing, svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from zmq.backend.cython.socket import cPickle

from src.learning import DATA_PATH

#classifier = LogisticRegression()
#classifier = DecisionTreeClassifier(random_state=2)
classifier = svm.SVC(probability=True)
#classifier = naive_bayes.MultinomialNB()
#scaler = preprocessing.MinMaxScaler()
scaler = StandardScaler()

STORAGE_PATH_CLASSIFIER = "models/var_detection_classifier.pkl"
STORAGE_PATH_SCALER = "models/var_detection_scaler.pkl"


def text_column_to_bow_column(text_data):
    count_vectorizer = CountVectorizer(max_features=2000, lowercase=False)#, stop_words=['english', 'german'])
    return count_vectorizer.fit_transform(text_data).toarray()


def test_classifier(df_path):
    training_df = pd.read_csv(df_path, sep='\t', header=None)
    text_data = training_df.iloc[:, 1:2].values.ravel()
    X = text_column_to_bow_column(text_data)
    y = training_df.iloc[:, 2:]
    #print(y)
    y = y.values.ravel()
    X = scaler.fit_transform(X, y)

    scores = cross_val_score(classifier, X, y, cv=5)
    print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
    #
    # X_train = scaler.fit_transform(X_train, y_train)
    # classifier.fit(X_train, y_train)
    # X_test = scaler.transform(X_test)
    # y_pred = classifier.predict(X_test)


def train_and_store_detection_classifier(df_path):

    training_df = pd.read_csv(df_path, sep='\t')
    text_data = training_df.iloc[:, 1:2].values.ravel()
    X = text_column_to_bow_column(text_data)
    y = training_df.iloc[:, 2:]
    y = y.values.ravel()
    X = scaler.fit_transform(X, y)
    classifier.fit(X, y)

    with open(STORAGE_PATH_CLASSIFIER , 'wb') as fid:
        cPickle.dump(classifier, fid)

    with open(STORAGE_PATH_SCALER , 'wb') as fid:
        cPickle.dump(scaler, fid)


def load_classifier_and_predict_variables(queries_file_path):

    with open(STORAGE_PATH_CLASSIFIER , 'rb') as fid:
        this_classifier = cPickle.load(fid)

    with open(STORAGE_PATH_SCALER , 'rb') as fid:
        this_scaler = cPickle.load(fid)

    text_data = pd.read_csv(queries_file_path, sep='\t')[1:2].values.ravel()
    X = text_column_to_bow_column(text_data)

    X = this_scaler.transform(X)
    y_pred = this_classifier.predict(X)
    text_data['is_variable'] = y_pred

    output_df = text_data.loc[text_data['is_variable'] != 0]
    output_df = output_df.iloc[:, :1]

    output_df.to_csv(queries_file_path, sep='\t', header=False, index=False)


df_path = DATA_PATH + "variable_detection/sv_ident_trial_train_and_val_variable_detection/variable_detection_df.tsv"
test_classifier(df_path)

