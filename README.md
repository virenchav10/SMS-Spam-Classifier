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