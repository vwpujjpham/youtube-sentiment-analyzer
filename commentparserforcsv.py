import pandas as pd
#for pipeline https://scikit-learn.org/stable/getting_started.html
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
#switched from LogisticReg to MultiNB bc. limited data. better baseline for text classification bc naturally models word occurence counts
from sklearn.naive_bayes import MultinomialNB
#Built in pre-processing (cleaning up data) (StandardScalar is for numerical features)
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#create a pipeline object
pipe = make_pipeline(
    TfidfVectorizer(
        stop_words="english",
        lowercase=True,
        #ngran_range: extracts both unigrams(single words) and bigrams(pairs of consecutive words) as features
        ngram_range=(1,2),
        max_features=5000,
        #sublinear_tf: dampens impact of very frequent words and avoids them dominating feature space. helps model focus on more informative words
        sublinear_tf=True
    ),
    MultinomialNB(
        alpha=0.5
    )
)
df = pd.read_csv("comments.csv")
X_text = df["text"]
like_count = df["like_count"]
y_sentiment = df["sentiment"]
#PREPROCESSING DATA: DATA CLEANUP
#fit: learn the vocabulary, figure out what words exist and how to assign importance scores.
#transform: converts the text comments into numeric vectors from information from fit.
#TURN DATA/WORDS INTO NUMBERS FOR MACHINE TO UNDERSTAND
#split data into 2 sets: 1 for training 1 for testing. test_size 0.2 means 20% data for testing, 80% training. random state=ensure split's reproducible
X_train, X_test, y_train, y_test = train_test_split(X_text, y_sentiment, test_size=0.2, random_state=42)
pipe.fit(X_train, y_train)
#Pipeline(steps=[('tfidfvectorizer', TfidfVectorizer()),
#                ('logisticregression', LogisticRegression())])
accuracy_score = pipe.score(X_test,y_test)
print("Test Accuracy: ", accuracy_score)
print(y_sentiment.value_counts())
print(classification_report(y_test, pipe.predict(X_test)))

def predict_sentiment(comment):
    if isinstance(comment, str):
        comment = [comment]
        prediction = pipe.predict(comment)
        return prediction