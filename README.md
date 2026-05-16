# 📩 SMS Spam Detection Classifier

A machine learning-based SMS spam detection system built using **Python**, **Scikit-learn**, and **Streamlit**, designed to classify SMS messages as **Spam** or **Ham (legitimate messages)** using Natural Language Processing techniques.

---

## 📌 Overview

This project builds and evaluates a machine learning spam classification system using the SMS Spam Collection dataset.

The system includes:

- **Multinomial Naive Bayes** for spam classification
- **TF-IDF Vectorization** for converting text into numerical features
- **Model comparison** using Logistic Regression and Linear SVM
- **Interactive Streamlit web application**
- **Single message prediction**
- **Bulk CSV batch classification**

The application is designed to detect spam patterns in text messages and can be extended to broader email or messaging spam detection use cases.

---

## 📂 Project Structure

```bash
.
├── sms.py                         # Streamlit web application
├── Untitled.ipynb                # Jupyter notebook for experimentation & model training
├── spam.csv                      # SMS spam dataset
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── models/
    └── sms_spam_classifier.pkl   # Trained machine learning model
```

---

## ⚙️ Features

- SMS spam detection using machine learning
- NLP preprocessing using TF-IDF vectorization
- Model comparison across multiple classifiers
- Interactive web UI using Streamlit
- Single message prediction
- Bulk CSV upload support
- Download prediction results as CSV
- Automatic support for common text column formats in uploaded datasets

---

## 📊 Dataset

This project uses the **SMS Spam Collection Dataset**, a public benchmark dataset for spam classification.

### Dataset Characteristics

- **Total messages:** 5,572
- **Ham (legitimate):** ~86.6%
- **Spam:** ~13.4%
- **Message type:** SMS text messages

### Typical Labels

```text
ham
spam
```

### Dataset Source

https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

---

## 🧠 Machine Learning Pipeline

The spam detection workflow follows:

```text
Raw SMS Text
   ↓
Text Cleaning
   ↓
Lowercasing
   ↓
Stopword Removal
   ↓
TF-IDF Vectorization
   ↓
Feature Extraction
   ↓
Multinomial Naive Bayes Classification
   ↓
Spam / Ham Prediction
```

### Models Explored

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Machine (SVM)

---

## 📈 Model Performance

Performance on the held-out test set:

- **Accuracy:** ~96%
- **Spam Precision:** 100%
- **Spam Recall:** ~72%
- Strong ham classification performance

### Evaluation Metrics Used

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/virenchav10/SMS-Spam-Classifier.git
cd SMS-Spam-Classifier
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Notebook (for experimentation)

```bash
jupyter notebook Untitled.ipynb
```

### 4️⃣ Run the Streamlit Application

```bash
streamlit run sms.py
```

---

## 💻 Web Application Features

### Single Message Prediction

Users can manually enter an SMS message for classification.

Example:

```text
FREE entry!! Win a brand new iPhone now!
```

Prediction:

```text
SPAM
```

---

### Bulk CSV Prediction

Users can upload CSV files for batch spam detection.

Supported text columns:

```text
message
text
v2
content
sms
body
Message
Text
```

### Example CSV

```csv
message
Hey, are we still meeting at 6?
FREE cash prize! Claim now!
Don't forget to bring milk
```

### Example Output

| message | prediction |
|--------|------------|
| Hey, are we still meeting at 6? | HAM |
| FREE cash prize! Claim now! | SPAM |

Results can be downloaded as CSV.

---

## 📜 Requirements

- Python 3.8+
- pandas
- scikit-learn
- streamlit
- joblib
- matplotlib
- seaborn

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🏗 Future Improvements

Potential future enhancements:

- Spam probability confidence scoring
- Email spam classification support
- Deep learning models (LSTM / BERT)
- REST API deployment
- Improved dashboard analytics
- Model explainability integration

---

## 🤝 Contributing

Pull requests are welcome. Feel free to fork the repository and submit improvements.

---

## 📄 License

This project is intended for educational and portfolio purposes.