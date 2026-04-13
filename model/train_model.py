import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

fake = pd.read_csv("data/Fake.csv")
real = pd.read_csv("data/True.csv")

fake["label"] = 0
real["label"] = 1

df = pd.concat([fake, real])
df = df[["text", "label"]]
df = df.sample(frac=1).reset_index(drop=True)

vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7, ngram_range=(1,2))
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression(max_iter=200)
model.fit(X, y)

pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Model trained successfully!")