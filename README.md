# 📩 SMS Spam Detection Classifier

A machine learning-based SMS spam detection system built using **Python**, **Scikit-learn**, and **Streamlit**, designed to classify text messages as **Spam** or **Ham (legitimate messages)** using Natural Language Processing techniques.

---

## 📌 Overview

This project implements an end-to-end spam detection pipeline using the SMS Spam Collection dataset.

The system includes:

- **TF-IDF Vectorization** for converting raw text into numerical features
- **Multinomial Naive Bayes** for spam classification
- **Model comparison** with Logistic Regression and Linear SVM
- **Interactive Streamlit web application**
- **Single message prediction**
- **Bulk CSV spam classification**
- **Downloadable prediction results**

The application can classify both manually entered messages and uploaded CSV datasets containing message text.

---

## 📂 Project Structure

```bash
.
├── sms.py                          # Streamlit web application
├── Untitled.ipynb                 # Jupyter notebook for experimentation & model training
├── spam.csv                       # SMS spam dataset
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── models/
    └── sms_spam_classifier.pkl    # Trained machine learning model

    ⚙️ Features

✅ SMS spam detection using machine learning
✅ NLP preprocessing using TF-IDF vectorization
✅ Model comparison across multiple classifiers
✅ Interactive web UI using Streamlit
✅ Single message prediction
✅ Bulk CSV upload support
✅ Download prediction results as CSV
✅ Handles multiple common text column formats in uploaded datasets

📊 Dataset

This project uses the SMS Spam Collection Dataset, a public benchmark dataset for spam classification.

Dataset characteristics:

5,572 SMS messages
Ham (legitimate): ~86.6%
Spam: ~13.4%

Typical labels:

ham
spam

Dataset source:

https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

🧠 Machine Learning Pipeline

The spam detection workflow follows:

Raw SMS Text
   ↓
Text Cleaning
   ↓
TF-IDF Vectorization
   ↓
Feature Extraction
   ↓
Multinomial Naive Bayes Classification
   ↓
Spam / Ham Prediction

Models explored:

Multinomial Naive Bayes
Logistic Regression
Linear Support Vector Machine (SVM)
📈 Model Performance

Performance on the held-out test set:

Accuracy: ~96%
Spam Precision: 100%
Spam Recall: ~72%
Strong Ham classification performance

Evaluation metrics used:

Accuracy
Precision
Recall
F1-score
Confusion Matrix
🚀 Installation
1️⃣ Clone the repository
git clone https://github.com/virenchav10/SMS-Spam-Classifier.git
cd SMS-Spam-Classifier
2️⃣ Install dependencies
pip install -r requirements.txt