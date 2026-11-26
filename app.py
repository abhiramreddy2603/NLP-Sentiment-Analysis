import re
import string

import joblib
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


@st.cache_resource
def load_nltk_resources():
    """Download the NLTK data required by the original preprocessing pipeline."""
    resources = {
        "corpora/stopwords": "stopwords",
        "tokenizers/punkt": "punkt",
        "tokenizers/punkt_tab": "punkt_tab",
        "corpora/wordnet": "wordnet",
    }

    for resource_path, package_name in resources.items():
        try:
            nltk.data.find(resource_path)
        except LookupError:
            if not nltk.download(package_name, quiet=True):
                raise RuntimeError(
                    f"Unable to download the NLTK resource: {package_name}"
                )

    return (
        WordNetLemmatizer(),
        set(stopwords.words("english")),
    )


@st.cache_resource
def load_model_artifacts():
    """Load the trained classifier and its matching TF-IDF vectorizer."""
    model = joblib.load("sentiment_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer


lemmatizer, stop_words = load_nltk_resources()
model, tfidf = load_model_artifacts()


def clean_text(text):
    """Apply the same text-cleaning steps used during model training."""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return " ".join(tokens)


st.set_page_config(
    page_title="Customer Review Sentiment Analysis",
    page_icon="💬",
    layout="centered",
)

st.title("Customer Review Sentiment Analysis")
st.write(
    "Enter a customer review to classify its sentiment as "
    "**Positive, Neutral, or Negative**."
)

review = st.text_area(
    "Enter your review:",
    placeholder="Example: The camera quality is excellent, but the battery drains quickly.",
    height=150,
)

if st.button("Predict Sentiment", type="primary"):
    if not review.strip():
        st.warning("Please enter a review.")
    else:
        cleaned_review = clean_text(review)

        if not cleaned_review:
            st.warning(
                "The review contains no usable text after preprocessing. "
                "Please enter a review with words."
            )
        else:
            features = tfidf.transform([cleaned_review])
            prediction = model.predict(features)[0]

            if prediction == "Positive":
                st.success(f"Predicted Sentiment: **{prediction}**")
            elif prediction == "Negative":
                st.error(f"Predicted Sentiment: **{prediction}**")
            else:
                st.info(f"Predicted Sentiment: **{prediction}**")

st.caption(
    "Educational project only. Predictions may be incorrect and should not "
    "be treated as definitive assessments of customer opinion."
)
