# NLP Sentiment Analysis

A machine learning project that analyses mobile customer reviews and classifies them into **Positive, Neutral, and Negative** sentiment categories. The project covers exploratory data analysis, text preprocessing, TF-IDF feature extraction, model comparison, evaluation, and an interactive Streamlit application.

## Live Application

**[Open the Customer Review Sentiment Analysis App](https://nlp-sentiment-analysis-valgymgjjmjax7gyxeu7jl.streamlit.app/)**

Enter a customer review into the application to receive a predicted sentiment: Positive, Neutral, or Negative.

## Project Objective

The objective of this project is to extract sentiment from customer reviews and provide an automated way to understand customer feedback.

The project workflow includes:

- Exploratory Data Analysis (EDA)
- Text preprocessing and cleaning
- Sentiment label creation from star ratings
- TF-IDF feature extraction
- Machine learning model training and evaluation
- Model comparison and best-model selection
- Sentiment prediction through a Streamlit application

## Dataset

The dataset contains **1,440 customer reviews** with the following columns:

| Column | Description |
|---|---|
| `title` | Customer review title |
| `rating` | Star rating |
| `body` | Customer review text |

The original dataset contains no missing values or duplicate rows.

### Sentiment Labeling

Sentiment categories were derived from the star ratings:

| Rating | Sentiment |
|---|---|
| 1–2 stars | Negative |
| 3 stars | Neutral |
| 4–5 stars | Positive |

After text cleaning, four empty reviews were removed, resulting in **1,436 usable reviews**.

### Final Sentiment Distribution

| Sentiment | Reviews | Percentage |
|---|---:|---:|
| Negative | 508 | 35.4% |
| Neutral | 199 | 13.9% |
| Positive | 729 | 50.8% |

The dataset is imbalanced, with Neutral having the fewest examples.

## Project Workflow

```text
Customer Reviews
       |
       v
Data Loading & Exploratory Data Analysis
       |
       v
Text Cleaning and Preprocessing
       |
       v
Sentiment Label Creation
       |
       v
Train-Test Split (80:20)
       |
       v
TF-IDF Feature Extraction
       |
       v
Model Training
       |
       v
Model Evaluation and Comparison
       |
       v
Best Model Selection
       |
       v
Save Model and TF-IDF Vectorizer
       |
       v
Streamlit Sentiment Prediction App
```

## Text Preprocessing

The review text is cleaned using the following steps:

- Convert text to lowercase
- Remove URLs
- Remove HTML tags
- Remove non-ASCII characters
- Remove punctuation
- Remove numbers
- Remove extra whitespace
- Tokenize the text
- Remove English stopwords
- Remove very short tokens
- Apply WordNet lemmatization

The same preprocessing approach is used by the Streamlit application before transforming new reviews.

## Feature Extraction

**TF-IDF (Term Frequency–Inverse Document Frequency)** is used to convert cleaned review text into numerical features.

Configuration:

- Maximum features: `5,000`
- Train-test split: `80:20`
- Stratified split
- Random state: `42`

The resulting split contains:

- Training set: **1,148 reviews**
- Test set: **288 reviews**

## Machine Learning Models

Three classification algorithms were trained and evaluated using the same TF-IDF features and test split:

1. **Logistic Regression**
2. **Random Forest** — 200 estimators
3. **Linear Support Vector Machine (Linear SVM)**

The models were evaluated using:

- Accuracy
- Weighted Precision
- Weighted Recall
- Weighted F1 Score
- Confusion Matrix

### Best Model

The **Linear SVM** achieved the best overall performance among the three evaluated models.

- Accuracy: approximately **75.7%**
- Weighted F1 Score: approximately **73.3%**

The Linear SVM performed better on Positive and Negative reviews. The Neutral class was more difficult to classify because it had fewer examples and customer reviews can contain mixed or ambiguous opinions.

## Streamlit Application

The project includes an interactive Streamlit application for predicting the sentiment of new customer reviews.

The application:

1. Accepts a customer review as text input.
2. Cleans and preprocesses the review.
3. Transforms the cleaned text using the saved TF-IDF vectorizer.
4. Passes the transformed features to the saved Linear SVM model.
5. Displays the predicted sentiment.

**[Try the deployed application](https://nlp-sentiment-analysis-valgymgjjmjax7gyxeu7jl.streamlit.app/)**

## Run the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/abhiramreddy2603/NLP-Sentiment-Analysis.git
cd NLP-Sentiment-Analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit

```bash
streamlit run app.py
```

The application will open in your browser.

The following files must be present in the repository root for prediction:

- `sentiment_model.pkl`
- `tfidf_vectorizer.pkl`

## Deployment

The application is hosted using **Streamlit Community Cloud** and connected to this GitHub repository.

- Deployment platform: Streamlit Community Cloud
- Application entry point: `app.py`
- Dependencies: `requirements.txt`

**Live URL:** https://nlp-sentiment-analysis-valgymgjjmjax7gyxeu7jl.streamlit.app/

## Repository Structure

```text
NLP-Sentiment-Analysis/
│
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

### File Description

| File | Description |
|---|---|
| `README.md` | Project documentation |
| `NLP_PROJECT.ipynb` | Project notebook containing EDA, preprocessing, model training and evaluation |
| `nlp_project.py` | Python implementation of the project |
| `dataset.xlsx` | Customer review dataset |
| `app.py` | Streamlit sentiment prediction application |
| `requirements.txt` | Python dependencies |
| `sentiment_model.pkl` | Saved best-performing Linear SVM model |
| `tfidf_vectorizer.pkl` | Fitted TF-IDF vectorizer |
| `Customer Review Sentiment.pptx` | Project presentation |

## Limitations

- Sentiment labels are derived from star ratings rather than manually annotated sentiment.
- The Neutral class has relatively few examples compared with Positive and Negative.
- Mixed or ambiguous reviews can be difficult to classify.
- Sarcasm and contextual meaning can be challenging for traditional TF-IDF-based models.
- The current model uses the review body for classification.
- Removing stopwords can remove negation terms that are important for sentiment, which is a limitation of the current preprocessing approach.

## Future Improvements

Possible improvements include:

- Increasing the number of Neutral training examples
- Hyperparameter tuning
- Cross-validation
- Experimenting with n-gram based TF-IDF features
- Testing class-weighting techniques
- Improving negation handling during text preprocessing
- Exploring contextual NLP models such as transformer-based models
- Extending the project toward aspect-based sentiment analysis

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- TF-IDF
- Matplotlib
- Seaborn
- WordCloud
- Joblib
- Streamlit
- Jupyter Notebook
- Google Colab

## Project Outcome

The project implements an end-to-end customer review sentiment analysis workflow, from dataset exploration and text preprocessing to model evaluation and an interactive deployed application.

The Linear SVM model was selected based on its highest weighted F1 score among the evaluated models. The trained model and TF-IDF vectorizer are used by the Streamlit application to classify new customer reviews.

---

*This project was completed as part of data science training and is intended for educational purposes.*
