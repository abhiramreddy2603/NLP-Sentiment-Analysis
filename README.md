# NLP Sentiment Analysis

A machine learning project for analyzing customer reviews and classifying them into **Positive, Neutral, and Negative** sentiment categories.

## Project Objective

The objective of this project is to extract sentiment from customer reviews and provide an automated way to understand customer feedback.

The project covers:

- Exploratory Data Analysis (EDA)
- Text preprocessing and cleaning
- Sentiment label creation from star ratings
- TF-IDF feature extraction
- Machine learning model training and evaluation
- Model comparison
- Sentiment prediction through a Streamlit application

## Dataset

The dataset contains **1,440 customer reviews** with the following columns:

- `title` — Review title
- `rating` — Star rating
- `body` — Customer review text

The original dataset contains no missing values or duplicate rows.

### Sentiment Labeling

The sentiment labels were derived from the star ratings:

| Rating | Sentiment |
|---|---|
| 1–2 stars | Negative |
| 3 stars | Neutral |
| 4–5 stars | Positive |

After text cleaning, empty reviews were removed, resulting in **1,436 usable reviews**.

Final sentiment distribution:

| Sentiment | Reviews | Percentage |
|---|---:|---:|
| Negative | 508 | 35.4% |
| Neutral | 199 | 13.9% |
| Positive | 729 | 50.8% |

The dataset is therefore somewhat imbalanced, with Neutral having the fewest examples.

## Project Workflow

```text
Customer Reviews
       ↓
Data Loading & EDA
       ↓
Text Cleaning
       ↓
Sentiment Label Creation
       ↓
Train-Test Split (80:20)
       ↓
TF-IDF Feature Extraction
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Best Model Selection
       ↓
Model & Vectorizer Serialization
       ↓
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
- Remove extra spaces
- Tokenize the text
- Remove English stopwords
- Remove very short tokens
- Apply WordNet lemmatization

## Feature Extraction

**TF-IDF (Term Frequency-Inverse Document Frequency)** is used to convert the cleaned review text into numerical features.

Configuration:

- Maximum features: `5000`
- Train-test split: `80:20`
- Stratified split
- Random state: `42`

The training set contains **1,148 reviews**, while the test set contains **288 reviews**.

## Machine Learning Models

Three classification algorithms were evaluated:

1. **Logistic Regression**
2. **Random Forest**
3. **Linear Support Vector Machine (SVM)**

The models were evaluated using:

- Accuracy
- Weighted Precision
- Weighted Recall
- Weighted F1 Score
- Confusion Matrix

### Best Model

The **Linear SVM** achieved the best overall performance among the three models.

- Accuracy: approximately **75.7%**
- Weighted F1 Score: approximately **73.3%**

The model performed best on Positive and Negative reviews, while the Neutral class was more difficult to classify because it had fewer examples and greater textual ambiguity.

## Model Files

The trained model and TF-IDF vectorizer are saved using Joblib:

```text
sentiment_model.pkl
tfidf_vectorizer.pkl
```

These files are loaded by the Streamlit application for making predictions on new reviews.

## Streamlit Application

The project includes a Streamlit application that allows a user to:

1. Enter a customer review.
2. Clean and preprocess the review.
3. Transform the review using the saved TF-IDF vectorizer.
4. Pass the features to the saved Linear SVM model.
5. Display the predicted sentiment.

### Run the Application

Install the required packages:

```bash
pip install -r requirements.txt
```

Then start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser and allow you to enter reviews for sentiment prediction.

## Repository Structure

```text
NLP-Sentiment-Analysis/
│
├── README.md
├── NLP_Sentiment_Analysis.ipynb
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
| `NLP_Sentiment_Analysis.ipynb` | Complete project notebook |
| `nlp_project.py` | Python version of the project code |
| `dataset.xlsx` | Customer review dataset |
| `app.py` | Streamlit sentiment prediction application |
| `requirements.txt` | Python dependencies for the application |
| `sentiment_model.pkl` | Trained best-performing sentiment model |
| `tfidf_vectorizer.pkl` | Fitted TF-IDF vectorizer |
| `Customer Review Sentiment.pptx` | Project presentation |

## Limitations

- Sentiment labels are derived from star ratings rather than manually annotated sentiment.
- The Neutral class has relatively few examples.
- Some reviews can contain mixed or ambiguous opinions.
- Sarcasm and contextual meaning can be difficult for traditional TF-IDF-based models.
- The current model uses the review body for classification.

## Future Improvements

Possible improvements include:

- Increasing the number of Neutral training examples
- Hyperparameter tuning
- Cross-validation
- Trying n-gram based TF-IDF features
- Using class-weighting techniques
- Experimenting with contextual NLP models such as transformer-based models
- Adding aspect-based sentiment analysis
- Improving deployment and monitoring

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- WordCloud
- Joblib
- Streamlit
- Jupyter Notebook / Google Colab

## Project Outcome

The project successfully implements an end-to-end customer review sentiment analysis pipeline, from raw review data and preprocessing through model evaluation and deployment preparation.

The **Linear SVM** model was selected as the final model based on the highest weighted F1 score among the evaluated models, and the trained model and TF-IDF vectorizer are provided for use by the Streamlit application.
