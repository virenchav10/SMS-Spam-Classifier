# SMS Spam Detection Classifier

A machine learning web app that predicts whether an SMS message is spam or ham. The project uses Python, Scikit-learn, TF-IDF vectorization, Naive Bayes classification, and Streamlit for the user interface.

## Features

- Single message spam prediction
- Bulk CSV upload prediction
- Download prediction results as CSV
- Text preprocessing using TF-IDF
- Naive Bayes classification model
- Simple Streamlit web interface

## Dataset

The model was trained using the SMS Spam Collection dataset. The dataset contains SMS messages labelled as either ham or spam.

## Model

The classifier uses:

- TF-IDF Vectorizer for converting text into numerical features
- Multinomial Naive Bayes for classification

## Performance

The model achieved around 96% accuracy on the test set.

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt