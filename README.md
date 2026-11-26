# NLP Sentiment Analysis

A machine learning project that analyses mobile customer reviews and classifies them into **Positive, Neutral, and Negative** sentiment categories. The project includes exploratory data analysis, text preprocessing, model comparison, and a Streamlit application for interactive predictions.

## Project Overview

The objective is to extract sentiment from customer review text and provide an automated way to understand customer feedback.

## Dataset

The dataset contains **1,440 customer reviews** with three columns:

- `title` — Review title
- `rating` — Star rating
- `body` — Customer review text

The original dataset contains no missing values or duplicate rows. Sentiment labels are derived from ratings:

| Rating | Sentiment |
|---|---|
| 1–2 stars | Negative |
| 3 stars | Neutral |
| 4–5 stars | Positive |

After text cleaning, four empty reviews were removed, leaving **1,436 usable reviews**.

| Sentiment | Reviews | Share |
|---|---:|---:|
| Negative | 508 | 35.4% |
| Neutral | 199 | 13.9% |
| Positive | 729 | 50.8% |

The classes are imbalanced, with fewer Neutral examples.

## Workflow

1. Exploratory Data Analysis (EDA)
2. Text cleaning and preprocessing
3. Sentiment label creation from star ratings
4. TF-IDF feature extraction
5. Train-test split (80:20, stratified, random state 42)
6. Model training and comparison
7. Evaluation using accuracy, weighted precision, weighted recall, weighted F1, and confusion matrices
8. Selection and serialization of the best model
9. Streamlit application for new review predictions

## Text Preprocessing

The training notebook and Streamlit application use the following steps:

- Convert text to lowercase
- Remove URLs and HTML tags
- Remove non-ASCII characters, punctuation, and numbers
- Normalize whitespace
- Tokenize text
- Remove English stopwords and tokens shorter than three characters
- Apply WordNet lemmatization

## Feature Extraction

TF-IDF converts cleaned review text into numerical features.

- Maximum features: `5,000`
- Training set: `1,148` reviews
- Test set: `288` reviews

## Models and Results

Three models were evaluated on the same held-out test set:

| Model | Accuracy | Weighted Precision | Weighted Recall | Weighted F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 74.31% | 71.11% | 74.31% | 69.21% |
| Random Forest | 72.22% | 62.76% | 72.22% | 66.48% |
| **Linear SVM** | **75.69%** | **73.94%** | **75.69%** | **73.40%** |

**Linear SVM** was selected because it achieved the highest weighted F1 score in this comparison.

The Neutral class was the most difficult to classify. Its F1 score for Linear SVM was approximately 0.30, reflecting the smaller number of Neutral examples and ambiguity in mixed customer reviews.

## Streamlit Application

The app accepts a customer review, applies the same text-cleaning steps, transforms it using the saved TF-IDF vectorizer, and predicts its sentiment using the saved Linear SVM model.

### Run Locally

Use Python 3.12 for the environment, then run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app requires these model files in the repository root:

- `sentiment_model.pkl`
- `tfidf_vectorizer.pkl`

## Deployment — Streamlit Community Cloud

1. Push the project files to a GitHub repository.
2. Confirm that `app.py`, `requirements.txt`, `sentiment_model.pkl`, and `tfidf_vectorizer.pkl` are in the repository root.
3. Open [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with GitHub.
4. Select **Create app**.
5. Choose this repository, the `main` branch, and `app.py` as the main file.
6. In Advanced settings, select **Python 3.12**.
7. Deploy the app and wait for the build to finish.
8. Test Positive, Negative, Neutral, empty, and punctuation-only review inputs.
9. Add the generated public app URL to this README under a **Live Application** heading.

Streamlit Community Cloud redeploys the app when repository changes are pushed to GitHub.

## Repository Structure

```text
NLP-Sentiment-Analysis/
├── README.md
├── NLP_PROJECT.ipynb
├── nlp_project.py
├── dataset.xlsx
├── app.py
├── requirements.txt
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
└── Customer Review Sentiment.pptx
```

## Limitations

- Sentiment labels are derived from star ratings rather than manually annotated sentiment.
- The Neutral class has fewer training examples.
- Sarcasm, mixed opinions, and contextual meaning can be difficult for traditional TF-IDF-based models.
- The current model uses the review body for classification.
- The app's output is a model prediction, not a guaranteed interpretation of a customer's intent.

## Technologies Used

Python, Pandas, NumPy, NLTK, Scikit-learn, TF-IDF, Matplotlib, Seaborn, WordCloud, Joblib, Streamlit, Jupyter Notebook, and Google Colab.

## Project Files

- `NLP_PROJECT.ipynb` — Project notebook, including EDA, preprocessing, training, and evaluation
- `nlp_project.py` — Python implementation
- `dataset.xlsx` — Customer review dataset
- `app.py` — Streamlit prediction application
- `sentiment_model.pkl` — Selected trained Linear SVM model
- `tfidf_vectorizer.pkl` — Fitted TF-IDF vectorizer
- `requirements.txt` — Application dependencies
- `Customer Review Sentiment.pptx` — Project presentation

## Future Improvements

- Increase the number of Neutral training examples
- Test n-gram features, class weighting, and hyperparameter tuning
- Evaluate with cross-validation
- Explore contextual NLP models
- Investigate negation handling and mixed-sentiment reviews
- Extend toward aspect-based sentiment analysis

---

*This project was completed as part of data science training. It is an educational machine-learning demonstration.*
